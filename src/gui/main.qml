
import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Window

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "Coin thing"
    property string currentTime: "00:00:00"
    property QtObject clock
    property QtObject coinStream
    Rectangle {
        anchors.fill: parent
        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./images/btc.jpg"
            fillMode: Image.PreserveAspectFit
        }
        ListModel{
            id: coinsModel
        }
        ListView {
            id: listView
            clip: true
            anchors.topMargin: 8
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: clickmeButton.top
            anchors.bottomMargin: 8
            anchors.leftMargin: 20
            width: 550
            height: 400
            model: coinsModel
            delegate: RowLayout {

                Text {
                    text: symbol
                    color: "white"
                }

                Text {
                    text: currentPrice
                    color: "white"
                }

                Text {
                    text: allTimeHigh
                    color: "white"
                }

                Text {
                    text: allTimeLow
                    color: "white"
                }

                Item { width: 100 }
            }

            ScrollBar.vertical: ScrollBar {}
            Connections {
                target: coinStream
                function onUpdated(coinsArray) {
                    // coinsModel.clear()
                    coinsArray.forEach(coin => {
                        coinsModel.append(
                            {symbol: coin.symbol, 
                            currentPrice: coin.current_price, 
                            allTimeHigh: coin.ath, 
                            allTimeLow: coin.atl
                        })
                    })
                }
            }

        }
        Button {
            id: clickmeButton
            anchors.right: parent.right
            anchors.rightMargin: 16
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 16

            text: 'Add Item'
            background: Rectangle {

                implicitWidth: 100
                implicitHeight: 40

                color: clickmeButton.down ? "#9ED624" : "#ABE827"
                radius: 4
            }

            onClicked: {
                console.log('clicked')
                var itemNum = listView.model.rowCount();
                console.log('num of items: ' + itemNum);
                var isChecked = Math.round(Math.random());

                listView.model.appendRow(`item_${itemNum}`, isChecked)
            }
        }
        Rectangle {
            anchors.fill: parent
            color: "transparent"
            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: currentTime
                font.pixelSize: 34
                color: "white"
            }
        }
    }
    Connections {
        target: clock
        function onUpdated(time) {
            currentTime = time;
        }
    }
}



