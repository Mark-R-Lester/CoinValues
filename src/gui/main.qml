
import QtQuick
import QtQuick.Controls.Basic
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Window

ApplicationWindow {
    id: root
    visible: true
    width: 600
    height: 500
    title: "Coin thing"
    property string currentTime: "00:00:00"
    property QtObject clock
    property QtObject coinStream
    Rectangle {
        id: coinFeed
        anchors.fill: parent
        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./images/btc.jpg"
            fillMode: Image.PreserveAspectFit
        }
        ListModel{
            id: fixedSupplyModel
        }
        ListModel{
            id: defiModel
        }
        ListModel{
            id: exchangeModel
        }
        RowLayout {
            id: coinHeaders
            anchors.left: parent.left
            anchors.leftMargin: 20
            anchors.top: parent.top
            anchors.topMargin: 14
            anchors.bottom: coinList.top
            anchors.bottomMargin: 14

            Rectangle {
                width: 100
                height: 30
                color: "#33000000"
                border.color: 'white'
                border.width: 0.1
                Text {
                    anchors.left: parent.left
                    anchors.leftMargin: 10
                    anchors.top: parent.top
                    anchors.topMargin: 7
                    opacity: 1
                    text: 'Rating'
                    color: "white"
                }
            }
            Rectangle {
                width: 100
                height: 30
                color: "#33000000"
                border.color: 'white'
                border.width: 0.1
                Text {
                    anchors.left: parent.left
                    anchors.leftMargin: 10
                    anchors.top: parent.top
                    anchors.topMargin: 7
                    opacity: 1
                    text: 'Symbol'
                    color: "white"
                }
            }
            Rectangle {
                width: 100
                height: 30
                color: "#33000000"
                border.color: 'white'
                border.width: 0.1
                Text {
                    anchors.left: parent.left
                    anchors.leftMargin: 10
                    anchors.top: parent.top
                    anchors.topMargin: 7
                    opacity: 1
                    text: 'Current Price'
                    color: "white"
                }
            }
            Rectangle {
                width: 100
                height: 30
                color: "#33000000"
                border.color: 'white'
                border.width: 0.1
                Text {
                    anchors.left: parent.left
                    anchors.leftMargin: 10
                    anchors.top: parent.top
                    anchors.topMargin: 7
                    opacity: 1
                    text: 'All Time High'
                    color: "white"
                }
            }
            Rectangle {
                width: 100
                height: 30
                color: "#33000000"
                border.color: 'white'
                border.width: 0.1
                Text {
                    anchors.left: parent.left
                    anchors.leftMargin: 10
                    anchors.top: parent.top
                    anchors.topMargin: 7
                    opacity: 1
                    text: 'All time Low'
                    color: "white"
                }
            }
        }
        ListView {
            id: coinList
            clip: true
            anchors.topMargin: 30
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top : coinHeaders.top
            anchors.bottomMargin: 8
            anchors.leftMargin: 20
            width: 550
            height: 400
            model: fixedSupplyModel
            delegate: RowLayout {
                id: coinRow

                Rectangle {
                    width: 100
                    height: 19
                    color: "#33000000"
                    border.color: 'white'
                    border.width: 0.1
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                        anchors.top: parent.top
                        anchors.topMargin: 1.75
                        opacity: 1
                        text: rating
                        color: "white"
                    }
                }

                Rectangle {
                    width: 100
                    height: 19
                    color: "#33000000"
                    border.color: 'white'
                    border.width: 0.1
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                        anchors.top: parent.top
                        anchors.topMargin: 1.75
                        opacity: 1
                        text: symbol
                        color: "white"
                    }
                }

                Rectangle {
                    width: 100
                    height: 19
                    color: "#33000000"
                    border.color: 'white'
                    border.width: 0.1
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                        anchors.top: parent.top
                        anchors.topMargin: 1.75
                        opacity: 1
                        text: currentPrice
                        color: "white"
                    }
                }

                Rectangle {
                    width: 100
                    height: 19
                    color: "#33000000"
                    border.color: 'white'
                    border.width: 0.1
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                        anchors.top: parent.top
                        anchors.topMargin: 1.75
                        opacity: 1
                        text: allTimeHigh
                        color: "white"
                    }
                }

                Rectangle {
                    width: 100
                    height: 19
                    color: "#33000000"
                    border.color: 'white'
                    border.width: 0.1
                    Text {
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                        anchors.top: parent.top
                        anchors.topMargin: 1.75
                        opacity: 1
                        text: allTimeLow
                        color: "white"
                    }
                }

                Item { width: 100 }
            }

            ScrollBar.vertical: ScrollBar {}
            Connections {
                target: root.coinStream
                function onUpdated(coins) {
                   root.updateModel(coins, fixedSupplyModel)
                }
            }

        }
        RowLayout{
             anchors.bottom: parent.bottom
             anchors.bottomMargin: 20
             anchors.right: parent.right
             anchors.rightMargin: 20

            Rectangle{
                width: 100
                height: 30
                color: "#33000000"
                border.color: 'white'
                border.width: 0.1
                Button {
                    id: fixexSupplyButton
                    text: 'Fixed supply'
                    background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 40
                        color: fixexSupplyButton.down ? "#9ED624" : "#ABE827"
                        radius: 4
                    }

                    onClicked: {
                        console.log('clicked')
                        coinList.model = fixedSupplyModel
                    }
                }
            }
            Rectangle{
                width: 100
                height: 30
                color: "#33000000"
                border.color: 'white'
                border.width: 0.1
                Button {
                    id: defiButton
                    text: 'DEFI'
                    background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 40
                        color: defiButton.down ? "#9ED624" : "#ABE827"
                        radius: 4
                    }

                    onClicked: {
                        console.log('clicked')
                        coinList.model = defiModel
                    }
                }
            }
            Rectangle{
                width: 100
                height: 30
                color: "#33000000"
                border.color: 'white'
                border.width: 0.1
                Button {
                    id: exchangeButton
                    text: 'Exchange'
                    background: Rectangle {
                        implicitWidth: 100
                        implicitHeight: 40
                        color: exchangeButton.down ? "#9ED624" : "#ABE827"
                        radius: 4
                    }

                    onClicked: {
                        console.log('clicked')
                        coinList.model = exchangeModel
                    }
                }
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
                text: root.currentTime
                font.pixelSize: 34
                color: "white"
            }
        }
    }
    Connections {
        target: root.clock
        function onUpdated(time) {
            currentTime = time;
        }
    }
    function updateModel(coins, model) {
        coins.forEach(coin => {
                model.append(
                    {
                        symbol: coin.symbol, 
                        currentPrice: coin.current_price, 
                        allTimeHigh: coin.ath, 
                        allTimeLow: coin.atl,
                        rating: coin.rating
                    }
                )
            function sortModel(model) {
                console.log('sorting')
                var n;
                var i;
                for (n=0; n < model.count; n++)
                    for (i=n+1; i < model.count; i++) {
                        if (model.get(n).rating < model.get(i).rating) {
                            model.move(i, n, 1);
                            n=0;
                        }
                    }
            }
            sortModel(model)
        })
    }
}



