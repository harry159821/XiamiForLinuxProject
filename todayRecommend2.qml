import QtQuick 1.0

Rectangle {
    id: root
    //width:1000; height:200
    //width: globalWidth; height:globalHeight
    //property int globalWidth;
    //property int globalHeight;
    color: "transparent"

    Rectangle {
        width:30; height:root.height
        color: "transparent"
        MouseArea {
        	id:leftMouseArea
        	anchors.fill: parent
        	hoverEnabled: true
        	onPressed:{
        		listPathView.decrementCurrentIndex()
        		leftButton.source="img/todayRecommend/arrow_left_down.tiff"
        	}
			onEntered:leftButton.source="img/todayRecommend/arrow_left_hover.tiff"
			onReleased:leftButton.source="img/todayRecommend/arrow_left_hover.tiff"	
			onExited:leftButton.source="img/todayRecommend/arrow_left_normal.tiff"
        }        
        Image {
        	id:leftButton
        	width:25; height:25
        	anchors.centerIn: parent
        	source:"img/todayRecommend/arrow_left_normal.tiff"
        	smooth:true
        }
    }

    Rectangle {
    	id:listRec
    	x:30;y:2
        width:root.width-60; height:root.height
        color: "transparent"

	    //列表模型
	    ListModel {
	    	//ID
	    	id:myModel
	    	//成员
	    	ListElement { picName: "pics/340126.jpg"     ;collectName:"触动心灵" 			;collectTime:"2014.08.17"}
	    	ListElement { picName: "pics/381815.jpg"     ;collectName:"你快乐所以我快乐" 	;collectTime:"2014.08.17"}
	    	ListElement { picName: "pics/485180.jpg"     ;collectName:"韩国日本选集" 		;collectTime:"2014.08.17"}
	    	ListElement { picName: "pics/1861261471.jpg" ;collectName:"经典选集" 			;collectTime:"2014.08.17"}
	    	ListElement { picName: "pics/1669845108.jpg" ;collectName:"触动心灵" 			;collectTime:"2014.08.17"}
	    	ListElement { picName: "pics/2081821708.jpg" ;collectName:"你快乐所以我快乐" 	;collectTime:"2014.08.17"}
	    	ListElement { picName: "pics/507984.jpg"     ;collectName:"韩国日本选集" 		;collectTime:"2014.08.17"}
	    }

	    //Model的代表组件构成结构
	    //可以理解成Model的每个组件遵循的结构？
	    Component {
	    	id:myDelegate
	    	Item {
	    		width:170; height:170    		
	    		//可见性 绑定path？
	    		visible: PathView.onPath

	    		Image {
	    			id:myImage
	    			width:170; height:170
	    			source: picName
	    			anchors.horizontalCenter: parent.horizontalCenter
	    			//平滑过度
	    			smooth:true
	    			z:0
	    		}

	    		Image {
	    			width:myImage.width; height:myImage.height
	    			source: "img/todayRecommend/collect_mask.png"
	    			smooth:true
	    			z:1
	    		}

	    		Text {
	    			y:myImage.height+1
	    			text:collectName
	    			font.pointSize: 10
	    			font.bold:true
	    			font.family: "微软雅黑"
	    		}

	    		Text {
	    			y:myImage.height+20
	    			text:collectTime
	    			font.pointSize: 8
	    		}

	            transform: [
	            ]    		
	    	}
	    }

	    PathView {
	    	id:listPathView
	    	focus:true
	    	model: myModel
	    	delegate: myDelegate
	    	anchors.fill: parent
	    	//path上容纳的Item数量
	    	pathItemCount: 4

	    	//属性设置弹簧效果的衰减速率,默认值为 100    	
	    	flickDeceleration: 400
	    	path: myPath

	    	//鼠标控制移动
	    	Keys.onLeftPressed:  decrementCurrentIndex()
	    	Keys.onRightPressed: incrementCurrentIndex()
	    }

		//图像行走的路线
	    Path {
	    	id: myPath
	    	//path的开始位置 及此刻的属性
	        startX:listRec.x+70; startY:root.height*4/10; //按比例

	        //PathLine{x:listRec.x-70; y:root.height*4/10}
	        
	        //结束位置
	        PathLine{x:root.width+30; y:root.height*4/10}
	    }
    }

    Rectangle {
    	x:root.width-30
        width:30; height:root.height
        color: "transparent"
        MouseArea {
        	id:rightMouseArea
        	anchors.fill: parent
        	hoverEnabled: true
        	onPressed:{
        		listPathView.incrementCurrentIndex()
        		rightButton.source="img/todayRecommend/arrow_right_down.tiff"
        	}
			onEntered:rightButton.source="img/todayRecommend/arrow_right_hover.tiff"
			onReleased:rightButton.source="img/todayRecommend/arrow_right_hover.tiff"
			onExited:rightButton.source="img/todayRecommend/arrow_right_normal.tiff"
        }        
        Image {
        	id:rightButton
        	width:25; height:25
        	anchors.centerIn: parent
        	source:"img/todayRecommend/arrow_right_normal.tiff"
        	smooth:true
        }
    }
}
