#!usr/evn/python
# -*- coding:utf-8 -*-
from PyQt4 import QtGui,QtCore
import sys

class SongTable(QtGui.QMainWindow):
    def __init__(self):
        super(SongTable, self).__init__()    
        self.centralwidget = QtGui.QWidget(self)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0,0,0,0)

        self.table = TableWidget(self.centralwidget)

        self.verticalLayout.addWidget(self.table)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.table.resize(500,300)
        self.table.horizontalHeader().setDefaultSectionSize(150)    # 默认宽度
        self.table.horizontalHeader().setClickable(True)            # 是否可点击
        
        self.table.setColumnCount(3)    # 列数
        self.table.setRowCount(6)      # 行数  

        self.table.setHorizontalHeaderLabels([u'歌名',u'时长',u'艺人'])

        # 表头字体
        font = self.table.horizontalHeader().font()
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)
        self.table.horizontalHeader().setStretchLastSection(True)                       # 设置充满表宽度
        self.table.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.table.verticalHeader().setDefaultSectionSize(10)                          # 设置行高
        self.table.setFrameShape(QtGui.QFrame.NoFrame)                                 # 设置无边框
        self.table.setShowGrid(False)                                                  # 设置不显示格子线
        self.table.verticalHeader().setVisible(False)                                  # 设置垂直头不可见
        self.table.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)         # 可多选（Ctrl、Shift、  Ctrl+A都可以）
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)            # 设置选择行为时每次选择一行
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)             # 设置不可编辑
        self.table.horizontalHeader().resizeSection(0,320)                             # 设置表头第一列的宽度为150
        self.table.horizontalHeader().resizeSection(1,60)                              # 设置表头第一列的宽度为150
        self.table.horizontalHeader().resizeSection(2,100)                             # 设置表头第一列的宽度为150
        self.table.horizontalHeader().setFixedHeight(25)                               # 设置表头的高度
        self.table.setStyleSheet("""
            QTableView {
                    border:none;
                    background:white;
            }
            QTableView::item:selected {
                    color:white;
                    background:rgb(37,52,60);    
            }          
            """)

        self.table.setFocusPolicy(QtCore.Qt.NoFocus) # 去除虚线框

        # 点击表时不对表头行光亮（获取焦点） 
        self.table.horizontalHeader().setHighlightSections(False)

        # 设置水平、垂直滚动条样式
        self.table.horizontalScrollBar().setStyleSheet("""
            QScrollBar{background:transparent; height:10px;}
            QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}
            QScrollBar::handle:hover{background:gray;}
            QScrollBar::sub-line{background:transparent;}
            QScrollBar::add-line{background:transparent;}
            """)
        self.table.verticalScrollBar().setStyleSheet("""
            QScrollBar{background:transparent; width: 10px;}
            QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px;}
            QScrollBar::handle:hover{background:gray;}
            QScrollBar::sub-line{background:transparent;}
            QScrollBar::add-line{background:transparent;}
            """)

        # 奇偶行变色
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(243, 246, 249))
        self.table.setPalette(palette)
        self.table.setAlternatingRowColors(True)

        # 信号
        self.table.cellDoubleClicked.connect(self.cellDoubleClickedSlot)

        self.resize(500,300)

    def cellDoubleClickedSlot(self,row,column):
        print "cellDoubleClickedSlot",row

    def setTestData(self):
        self.setRowData(0,['Amazing','5:57','Aerosmith'])
        self.setRowData(1,['Dream On','4:25','Aerosmith'])
        self.setRowData(2,['The Title','1:10','The Author'])
        self.setRowData(3,["Can't Smile Without You",'3:13','Barry Marilow'])
        self.setRowData(4,['Bic Runga-Listening For The Weather','3:32','bic runga'])
        self.setRowData(5,['THE STROKE','3:39','BILLY SQUIER'])

        self.setRowData(6,['Amazing','5:57','Aerosmith'])
        self.setRowData(7,['Dream On','4:25','Aerosmith'])
        self.setRowData(8,['The Title','1:10','The Author'])
        self.setRowData(9,["Can't Smile Without You",'3:13','Barry Marilow'])
        self.setRowData(10,['Bic Runga-Listening For The Weather','3:32','bic runga'])
        self.setRowData(11,['THE STROKE','3:39','BILLY SQUIER'])

        self.addRow(['THE STROKE','3:39','BILLY SQUIER'])
        self.addRow(['THE STROKE2','3:39','BILLY SQUIER'])
        self.addRow(['THE STROKE3','3:39','BILLY SQUIER'])
        self.addRow(['THE STROKE4','3:39','BILLY SQUIER'])
        self.addRow(['THE STROKE5','3:39','BILLY SQUIER'])
        self.addRow()
        self.addRow()
        self.addRow()

    def setRowData(self,row,dataList=['None','None','None']):
        if self.table.rowCount()<=row:
            for newRow in range(self.table.rowCount(),row+1):
                self.table.insertRow(newRow)                
        for column in range(0,len(dataList)):
            newItem = QtGui.QTableWidgetItem(dataList[column])
            self.table.setItem(row,column,newItem)

    def addRow(self,dataList=['None','None','None']):
        print dataList
        self.table.insertRow(self.table.rowCount())             
        for column in range(0,len(dataList)):
            newItem = QtGui.QTableWidgetItem(dataList[column])
            self.table.setItem(self.table.rowCount()-1,column,newItem)

    def resizeEvent(self,event):
        if self.size().width()>360:
            self.table.horizontalHeader().resizeSection(0,self.size().width()-160)

class TableWidget(QtGui.QTableWidget):
    def __init__(self,parent):
        super(TableWidget, self).__init__(parent)
        self.pop_menu = QtGui.QMenu();
        self.action_name = QtGui.QAction(self)
        self.action_size = QtGui.QAction(self)
        self.action_type = QtGui.QAction(self)
        self.action_date = QtGui.QAction(self)
        self.action_open = QtGui.QAction(self);  
        self.action_download = QtGui.QAction(self)
        self.action_flush = QtGui.QAction(self)
        self.action_delete = QtGui.QAction(self)
        self.action_rename = QtGui.QAction(self)
        self.action_create_folder = QtGui.QAction(self)
 
        self.action_open.setText(u"打开")
        self.action_download.setText(u"下载")
        self.action_flush.setText(u"刷新")
        self.action_delete.setText(u"删除")
        self.action_rename.setText(u"重命名")
        self.action_create_folder.setText(u"新建文件夹")
        self.action_name.setText(u"名称")
        self.action_size.setText(u"大小")
        self.action_type.setText(u"项目类型")
        self.action_date.setText(u"修改日期")
   
        # 设置快捷键
        self.action_flush.setShortcut(QtGui.QKeySequence.Refresh)
 
        # 设置文件夹图标
        # action_create_folder.setIcon(icon)
        # QObject::connect(action_create_folder, SIGNAL(triggered()), self, SLOT(createFolder()))

        # 鼠标划过变色
        self.setMouseTracking(True)
        self.cellEntered.connect(self.cellEnteredSlot)

    def cellEnteredSlot(self,row,column):        
        # print row,       # 行
        # print column  # 列
        # print self.row(self.item(row,column)) # .setStyleSheet("""color:white;background:lightblue;""")
        # print self.cellWidget(row,column) # .setStyleSheet("""color:white;background:lightblue;""")
        # print self.item(row,column)
        pass

    def contextMenuEvent(self,event):
        self.pop_menu.clear() # 清除原有菜单
        point = event.pos() # 得到窗口坐标
        item = self.itemAt(point)
        # if item:
        if True:
            self.pop_menu.addAction(self.action_download)
            self.pop_menu.addAction(self.action_flush)
            self.pop_menu.addSeparator()
            self.pop_menu.addAction(self.action_delete)
            self.pop_menu.addAction(self.action_rename)
            self.pop_menu.addSeparator()
            self.pop_menu.addAction(self.action_create_folder)
            sort_style = self.pop_menu.addMenu(u"排序")
            sort_style.addAction(self.action_name)
            sort_style.addAction(self.action_size)
            sort_style.addAction(self.action_type)
            sort_style.addAction(self.action_date)
      
            # 菜单出现的位置为当前鼠标的位置
            self.pop_menu.exec_(QtGui.QCursor.pos())
            event.accept()

    def onHeaderClicked(self,column):
        print "onHeaderClicked:",column

    def getSelectedRow(self):# ,set_row):
        items = self.selectedItems()
        item_count = items.count()
        if(item_count <= 0):
            return False
        for i in range(0,item_count):
            # 获取选中的行
            item_row = self.row(items.at(i))
            # set_row.insert(item_row)
            self.insert(item_row)
        return True

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    songTable = SongTable()
    songTable.show()
    sys.exit(app.exec_())

"""
    void cellActivated(int row, int column)
    void cellChanged(int row, int column)
    void cellClicked(int row, int column)
    void cellDoubleClicked(int row, int column)
    void cellEntered(int row, int column)
    void cellPressed(int row, int column)
    void itemActivated(QTableWidgetItem *item)
    void itemChanged(QTableWidgetItem *item)
    void itemClicked(QTableWidgetItem *item)
    void itemDoubleClicked(QTableWidgetItem *item)
    void itemEntered(QTableWidgetItem *item)
    void itemPressed(QTableWidgetItem *item)
    void itemSelectionChanged()
    void currentItemChanged(QTableWidgetItem *current, QTableWidgetItem *previous)
    void currentCellChanged(int currentRow, int currentColumn, int previousRow, int previousColumn)
"""