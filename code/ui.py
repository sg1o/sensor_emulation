gui_str = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>431</width>
    <height>700</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="minimumSize">
   <size>
    <width>411</width>
    <height>700</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>431</width>
    <height>700</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Control Panel</string>
  </property>
  <property name="styleSheet">
   <string notr="true">QMainWindow {
    background-color:#ececec;
}
QPushButton, QToolButton, QCommandLinkButton{
    padding: 0 5px 0 5px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-width: 2px;
    border-radius: 8px;
    color: #616161;
    font-weight: bold;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #fbfdfd, stop:0.5 #ffffff, stop:1 #fbfdfd);
}
QPushButton::default, QToolButton::default, QCommandLinkButton::default{
    border: 2px solid transparent;
    color: #FFFFFF;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);
}
QPushButton:hover, QToolButton:hover, QCommandLinkButton:hover{
    color: #3d3d3d;
}
QPushButton:pressed, QToolButton:pressed, QCommandLinkButton:pressed{
    color: #aeaeae;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);
}
QPushButton:disabled, QToolButton:disabled, QCommandLinkButton:disabled{
    color: #616161;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #dce7eb, stop:0.5 #e0e8eb, stop:1 #dee7ec);
}
QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QTimeEdit, QDateEdit, QDateTimeEdit {
    border-width: 2px;
    border-radius: 8px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    background-color: #f4f4f4;
    color: #3d3d3d;
}
QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QTimeEdit:focus, QDateEdit:focus, QDateTimeEdit:focus {
    border-width: 2px;
    border-radius: 8px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);
    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #85b7e3, stop:1 #9ec1db);
    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);
    background-color: #f4f4f4;
    color: #3d3d3d;
}
QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled, QTimeEdit:disabled, QDateEdit:disabled, QDateTimeEdit:disabled {
    color: #b9b9b9;
}
QSpinBox::up-button, QDoubleSpinBox::up-button, QTimeEdit::up-button, QDateEdit::up-button, QDateTimeEdit::up-button {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    color: #272727;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    padding: 3px;
}
QSpinBox::down-button, QDoubleSpinBox::down-button, QTimeEdit::down-button, QDateEdit::down-button, QDateTimeEdit::down-button {
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    width: 15px;
    color: #272727;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-bottom-right-radius: 3px;
    padding: 3px;
}
QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed, QTimeEdit::up-button:pressed, QDateEdit::up-button:pressed, QDateTimeEdit::up-button:pressed {
    color: #aeaeae;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);
}
QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed, QTimeEdit::down-button:pressed, QDateEdit::down-button:pressed, QDateTimeEdit::down-button:pressed {
    color: #aeaeae;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);
}
QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover, QTimeEdit::up-button:hover, QDateEdit::up-button:hover, QDateTimeEdit::up-button:hover {
    color: #FFFFFF;
    border-top-right-radius: 5px;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);
    
}
QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover, QTimeEdit::down-button:hover, QDateEdit::down-button:hover, QDateTimeEdit::down-button:hover {
    color: #FFFFFF;
    border-bottom-right-radius: 5px;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);
}
QSpinBox::up-arrow, QDoubleSpinBox::up-arrow, QTimeEdit::up-arrow, QDateEdit::up-arrow, QDateTimeEdit::up-arrow {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-up-symbolic.symbolic.png);
}
QSpinBox::down-arrow, QDoubleSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow, QDateTimeEdit::down-arrow {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png);
}
QProgressBar {
    max-height: 8px;
    text-align: center;
    font: italic bold 11px;
    color: #3d3d3d;
    border: 1px solid transparent;
    border-radius:4px;
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);
}
QProgressBar::chunk {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
    border-radius: 4px;
}
QProgressBar:disabled {
    color: #616161;
}
QProgressBar::chunk:disabled {
    background-color: #aeaeae;
}
QSlider::groove {
    border: 1px solid #bbbbbb;
    background-color: #52595d;
    border-radius: 4px;
}
QSlider::groove:horizontal {
    height: 6px;
}
QSlider::groove:vertical {
    width: 6px;
}
QSlider::handle:horizontal {
    background: #ffffff;
    border-style: solid;
    border-width: 1px;
    border-color: rgb(207,207,207);
    width: 12px;
    margin: -5px 0;
    border-radius: 7px;
}
QSlider::handle:vertical {
    background: #ffffff;
    border-style: solid;
    border-width: 1px;
    border-color: rgb(207,207,207);
    height: 12px;
    margin: 0 -5px;
    border-radius: 7px;
}
QSlider::add-page, QSlider::sub-page {
    border: 1px transparent;
    background-color: #52595d;
    border-radius: 4px;
}
QSlider::add-page:horizontal {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);
}
QSlider::sub-page:horizontal {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
}
QSlider::add-page:vertical {
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
}
QSlider::sub-page:vertical {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);
}
QSlider::add-page:horizontal:disabled, QSlider::sub-page:horizontal:disabled, QSlider::add-page:vertical:disabled, QSlider::sub-page:vertical:disabled {
    background: #b9b9b9;
}
QComboBox, QFontComboBox {
    border-width: 2px;
    border-radius: 8px;
    border-style: solid;
    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);
    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);
    background-color: #f4f4f4;
    color: #272727;
    padding-left: 5px;
}
QComboBox:editable, QComboBox:!editable, QComboBox::drop-down:editable, QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: #ffffff;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    color: #272727;
    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}
QComboBox::down-arrow {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png); /*Adawaita icon thene*/
}

QComboBox::down-arrow:on {
    top: 1px;
    left: 1px;
}
QComboBox QAbstractItemView {
    border: 1px solid darkgray;
    border-radius: 8px;
    selection-background-color: #dadada;
    selection-color: #272727;
    color: #272727;
    background: white;
}
QLabel, QCheckBox, QRadioButton {
    color: #272727;
}
QCheckBox {
    padding: 2px;
}
QCheckBox:disabled, QRadioButton:disabled {
    color: #808086;
    padding: 2px;
}

QCheckBox:hover {
    border-radius:4px;
    border-style:solid;
    padding-left: 1px;
    padding-right: 1px;
    padding-bottom: 1px;
    padding-top: 1px;
    border-width:1px;
    border-color: transparent;
}
QCheckBox::indicator:checked {
    image: url(/usr/share/icons/Adwaita/16x16/actions/object-select-symbolic.symbolic.png);
    height: 15px;
    width: 15px;
    border-style:solid;
    border-width: 1px;
    border-color: #48a5fd;
    color: #ffffff;
    border-radius: 3px;
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #48a5fd, stop:0.5 #329cfb, stop:1 #48a5fd);
}
QCheckBox::indicator:unchecked {
    
    height: 15px;
    width: 15px;
    border-style:solid;
    border-width: 1px;
    border-color: #48a5fd;
    border-radius: 3px;
    background-color: #fbfdfa;
}
QLCDNumber {
    color: #616161;;
}
QMenuBar {
    background-color: #ececec;
}
QMenuBar::item {
    color: #616161;
    spacing: 3px;
    padding: 1px 4px;
    background-color: #ececec;
}

QMenuBar::item:selected {
    background-color: #dadada;
    color: #3d3d3d;
}
QMenu {
    background-color: #ececec;
}
QMenu::item:selected {
    background-color: #dadada;
    color: #3d3d3d;
}
QMenu::item {
    color: #616161;;
    background-color: #e0e0e0;
}
QTabWidget {
    color:rgb(0,0,0);
    background-color:#000000;
}
QTabWidget::pane {
    border-color: #050a0e;
    background-color: #e0e0e0;
    border-width: 1px;
    border-radius: 4px;
    position: absolute;
    top: -0.5em;
    padding-top: 0.5em;
}

QTabWidget::tab-bar {
    alignment: center;
}

QTabBar::tab {
    border-bottom: 1px solid #c0c0c0;
    padding: 3px;
    color: #272727;
    background-color: #fefefc;
    margin-left:0px;
}
QTabBar::tab:!last {
    border-right: 1px solid;
    border-right-color: #c0c0c0;
    border-bottom-color: #c0c0c0;
}
QTabBar::tab:first {
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
}
QTabBar::tab:last {
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
    color: #FFFFFF;
    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);
}
QRadioButton::indicator {
    height: 14px;
    width: 14px;
    border-style:solid;
    border-radius:7px;
    border-width: 1px;
}
QRadioButton::indicator:checked {
    border-color: #48a5fd;
    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #ffffff, stop:0.5 #ffffff, stop:0.6 #48a5fd, stop:1 #48a5fd);
}
QRadioButton::indicator:!checked {
    border-color: #a9b7c6;
    background-color: #fbfdfa;
}
QStatusBar {
    color:#027f7f;
}

QDial {
    background: #16a085;
}

QToolBox {
    color: #a9b7c6;
    background-color: #222b2e;
}
QToolBox::tab {
    color: #a9b7c6;
    background-color:#222b2e;
}
QToolBox::tab:selected {
    color: #FFFFFF;
    background-color:#222b2e;
}
QScrollArea {
    color: #FFFFFF;
    background-color:#222b2e;
}

QScrollBar:horizontal {
	max-height: 10px;
	border: 1px transparent grey;
	margin: 0px 20px 0px 20px;
	background: transparent;
}
QScrollBar:vertical {
	max-width: 10px;
	border: 1px transparent grey;
	margin: 20px 0px 20px 0px;
	background: transparent;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
	background: #52595d;
	border-style: transparent;
	border-radius: 4px;
	min-height: 25px;
}
QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {
	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
}
QScrollBar::add-line, QScrollBar::sub-line {
    border: 2px transparent grey;
    border-radius: 4px;
    subcontrol-origin: margin;
    background: #b9b9b9;
}
QScrollBar::add-line:horizontal {
    width: 20px;
    subcontrol-position: right;
}
QScrollBar::add-line:vertical {
    height: 20px;
    subcontrol-position: bottom;
}
QScrollBar::sub-line:horizontal {
    width: 20px;
    subcontrol-position: left;
}
QScrollBar::sub-line:vertical {
    height: 20px;
    subcontrol-position: top;
}
QScrollBar::add-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed, QScrollBar::sub-line:vertical:pressed {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
QScrollBar::up-arrow:vertical {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-up-symbolic.symbolic.png);
}
QScrollBar::down-arrow:vertical {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png);
}
QScrollBar::left-arrow:horizontal {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-previous-symbolic.symbolic.png);
}
QScrollBar::right-arrow:horizontal {
    image: url(/usr/share/icons/Adwaita/16x16/actions/go-next-symbolic.symbolic.png);
}</string>
  </property>
  <property name="locale">
   <locale language="Spanish" country="Spain"/>
  </property>
  <property name="animated">
   <bool>false</bool>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="set_temp">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>120</y>
      <width>45</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Set</string>
    </property>
   </widget>
   <widget class="QPushButton" name="set_hum">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>250</y>
      <width>45</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Set</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>310</y>
      <width>431</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Consumo eléctrico</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>430</y>
      <width>431</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="text">
     <string>Sensor de Presencia</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>200</y>
      <width>431</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Timer sensor de Humedad</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>-80</x>
      <y>60</y>
      <width>591</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Timer sensor de Temperatura</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QPushButton" name="send_cons">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>360</y>
      <width>71</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Send</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="temp_text">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>120</y>
      <width>141</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="alignment">
     <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="cons_text">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>360</y>
      <width>141</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="alignment">
     <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_5">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>360</y>
      <width>45</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>13</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>kW</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="readOnly">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_7">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>120</y>
      <width>45</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>13</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>s.</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="readOnly">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_8">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>250</y>
      <width>45</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>13</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>s.</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="readOnly">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLineEdit" name="hum_text">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>250</y>
      <width>141</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="alignment">
     <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="principal_text">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>20</y>
      <width>431</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Control Panel: Zone 1</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
    <property name="readOnly">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QPushButton" name="temp_cancel">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>120</y>
      <width>91</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Cancel</string>
    </property>
   </widget>
   <widget class="QPushButton" name="hum_cancel">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>250</y>
      <width>91</width>
      <height>45</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Cancel</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>540</y>
      <width>431</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="text">
     <string>Sensor de Luminosidad</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QScrollBar" name="scroll_lum">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>580</y>
      <width>300</width>
      <height>25</height>
     </rect>
    </property>
    <property name="sizePolicy">
     <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
      <horstretch>0</horstretch>
      <verstretch>0</verstretch>
     </sizepolicy>
    </property>
    <property name="minimumSize">
     <size>
      <width>300</width>
      <height>25</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>300</width>
      <height>10</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="maximum">
     <number>100</number>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>580</y>
      <width>51</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="text">
     <string>Min.</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>580</y>
      <width>51</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="text">
     <string>Max.</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QRadioButton" name="presen_switch">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>470</y>
      <width>171</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Presencia</string>
    </property>
    <property name="iconSize">
     <size>
      <width>30</width>
      <height>30</height>
     </size>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>-20</x>
      <y>630</y>
      <width>361</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="text">
     <string>Valor luminosidad actual:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="scroll_value">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>630</y>
      <width>81</width>
      <height>25</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>FreeMono</family>
      <pointsize>14</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>0</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
    </property>
    <property name="readOnly">
     <bool>true</bool>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""

b64_icon = b'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u7eee+65iL8u4Er//v29FStW6Iwzzojo65Ye/9q0acPxD6gF6x2QiTUQY3784x97o0ePjuhrJicna+7cuerXrx8nFcBpOnfu7L322mvKzMyM2Gv27NlT8+fP54FliDmdO3f2Vq5cqc6dO0fk9RISEvTcc8+pb9++7GtALVnvgEysgRj0l7/8RSNGjIjIa+Xk5OjNN9/U0KFDOakAKtCnTx9v9erVisRH4l1zzTVaunSp6tevzz6JmHTmmWd6q1at0hVXXFGnr5OWlqZXX31V119/PfsaEAbWOyATayAGJScne7Nnz/YWLFig7t2719nrXHzxxVq/fr369OnDSQVQhY4dO3offPCBrrvuujr5+RkZGXriiSc0d+5cpaWlsU8iptWrV89bsGCBpk+fruTk5LD//LPPPlurV6/WkCFD2NeAMLHeAZlYAzFs0KBB3gcffOAtW7ZM11xzTdguqp1xxhl69tln9e677+qMM87gpAKopkaNGnkvvfSS99e//lUdO3YMy8+Mi4vTsGHDtHnzZt12222e5/qjAQAjPM/zxo0b523cuFGXXnppWH5mQkKCxo8fr/Xr1+ucc85hXwPCyHoHZGINQBdffLH3yiuveJ999pkefPDBGt971qtXLz3zzDPasWOHxo4dywk8UEODBw/2Nm3apPnz56t///41uuDdoEED3XLLLdqyZYvmzJnjtWjRgv0RKEe7du28t956y1u6dKn69+9fo4+ljI+P1/XXX69Nmzbp0Ucf9TIyMtjfgDCz3gHLduiT/8TEGohNTZs29SZNmqRJkyZp165d/vLly7V27Vpt2bJFn376qQ4ePKh9+/YpPT1dWVlZatmypdq3b69evXqpb9++atmyJScSQJh4nucNGTJEQ4YM0TfffOMvWLBAa9as0YYNG7R9+3bt37//5J+Nj49XXl6eOnXqpG7duqlfv3665JJL+GgfIAR9+/b1+vbtq507d/ovvfSS3n77bb3//vsqLCws98+npKSoV69eGjhwoK6//no1adKE/Q2oQ9aLddkOfbJYM7EG0KpVK69Vq1YaO3as6yhAzMvJyfFuuOEG3XDDDSe/VlJS4hcUFCghIUH16tXjhB4Ik9atW5+8yFxYWOjv3LlTn332mQ4ePChJyszMVMuWLdWqVSsuXgERZH24Wm6xZmINAIBtcXFxXv369V3HAKJaUlKS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'