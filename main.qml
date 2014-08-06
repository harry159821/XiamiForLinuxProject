import QtQuick 1.0

Rectangle {
    width:1000; height:400
    color: "transparent"

    //列表模型
    ListModel {
    	//ID
    	id:myModel
    	//成员
    	ListElement { picName: "pics/340126.jpg"     }
    	ListElement { picName: "pics/381815.jpg"     }
    	ListElement { picName: "pics/485180.jpg"     }
    	ListElement { picName: "pics/1861261471.jpg" }
    	ListElement { picName: "pics/1669845108.jpg" }
    	ListElement { picName: "pics/2081821708.jpg" }
    	ListElement { picName: "pics/507984.jpg"     }
    }

    //Model的代表组件构成结构
    //可以理解成Model的每个组件遵循的结构？
    Component {
    	id:myDelegate
    	Item {
    		property real scaleValue: PathView.scalePic
    		width:300; height:300    		
    		//可见性 绑定path？
    		visible: PathView.onPath
    		//层次 绑定path？
    		z:PathView.zOrder

    		Image {
    			id:myImage
    			width:300; height:300+1
    			source: picName
    			anchors.horizontalCenter: parent.horizontalCenter
    			//平滑过度
    			smooth:true
    		}
    		Image {
    			id:subImage
    			width:300-2; height:300
    			source: picName
    			anchors.horizontalCenter: parent.horizontalCenter
    			smooth:true
    			//翻转
    			transform: Rotation {
    				origin.x:0; origin.y:300
    				axis{
    					x:1; y:0; z:0
    				}
    				angle:180
    			}
    		}
            Rectangle {
                y: myImage.height;
                x: -1
                width: myImage.width + 2
                height: myImage.height
                gradient: Gradient {
                    GradientStop { position: 0.0; color: Qt.rgba(0,0,0, 0.6) }
                    GradientStop { position: 0.2; color: Qt.rgba(255,255,255, 1.0) }
                }
            }

            transform: [
                Scale {
                    xScale:scaleValue; yScale:scaleValue
                    origin.x: 340/2;   origin.y: 260/2
                }
            ]    		
    	}
    }

    PathView {
    	focus:true
    	model: myModel
    	delegate: myDelegate
    	anchors.fill: parent
    	//path上容纳的Item数量
    	pathItemCount: 5

    	//设置突出选项
    	preferredHighlightBegin: 0.5
    	preferredHighlightEnd:   0.5
    	highlightRangeMode: PathView.StrictlyEnforceRange

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
    	startX:50; startY:170
        PathAttribute {name: "scalePic"; value: 0.5}
        PathAttribute {name: "zOrder"; value: 1}

        //中心位置
        PathLine{x:500; y:170}
        PathPercent {value: 0.50}
        PathAttribute {name: "scalePic"; value: 1}
        PathAttribute {name: "zOrder"; value: 3}

        //结束位置
        PathLine{x:950; y:170}
        PathPercent {value: 1.00}
        PathAttribute {name: "scalePic"; value: 0.5}
        PathAttribute {name: "zOrder"; value: 1}
    }
}
