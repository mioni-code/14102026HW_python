from PyQt6.QtWidgets import QGridLayout, QMainWindow,QFrame , QScrollArea, QVBoxLayout,QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from modules.app import app 


main_window = QMainWindow()

WIDTH_WINDOW = 1024
HEIGHT_WINDOW  = 800

# получаем обьект экрана
primary_screen = app.primaryScreen()
# получаем размеры экрана
screen_size = primary_screen.size()
# получаем ширину экрана
width_screen = screen_size.width()
# получаем высоту экрана
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)

main_frame = QFrame(parent=main_window)
main_frame.setStyleSheet("background-color: grey")
main_frame.setFixedSize(1024, 800)
main_frame_layout = QGridLayout()
main_frame_layout.setContentsMargins(20, 20, 20, 20)
main_frame_layout.setSpacing(10)
main_frame.setLayout(main_frame_layout)


frame_red1 = QFrame(parent=main_frame)
frame_red1.setStyleSheet("background-color: red")
main_frame_layout.addWidget(frame_red1, 0, 0)

frame_red2 = QFrame(parent=main_frame)
frame_red2.setStyleSheet("background-color: red")
main_frame_layout.addWidget(frame_red2, 0, 1)

frame_red3 = QFrame(parent=main_frame)
frame_red3.setStyleSheet("background-color: red")
main_frame_layout.addWidget(frame_red3, 0, 2)

frame_red1_layout = QHBoxLayout()
frame_red1_layout.setContentsMargins(20, 20, 20, 20)
frame_red1_layout.setSpacing(50)
frame_red1_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
frame_red1.setLayout(frame_red1_layout)

frame_white1 = QFrame(parent=frame_red1)
frame_white1.setStyleSheet("background-color: white")
frame_white1.setFixedSize(60, 60)
frame_red1_layout.addWidget(frame_white1)

frame_white2 = QFrame(parent=frame_red1)
frame_white2.setStyleSheet("background-color: lightgrey")
frame_white2.setFixedSize(60, 60)
frame_red1_layout.addWidget(frame_white2)

frame_red3_layout = QHBoxLayout()
frame_red3_layout.setContentsMargins(20, 20, 20, 20)
frame_red3_layout.setSpacing(50)
frame_red3_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
frame_red3.setLayout(frame_red3_layout)

frame_white3 = QFrame(parent=frame_red3)
frame_white3.setStyleSheet("background-color: white")
frame_white3.setFixedSize(60, 60)
frame_red3_layout.addWidget(frame_white3)

frame_white4 = QFrame(parent=frame_red3)
frame_white4.setStyleSheet("background-color: lightgrey")
frame_white4.setFixedSize(60, 60)
frame_red3_layout.addWidget(frame_white4)

frame_green1 = QFrame(parent=main_frame)
frame_green1.setStyleSheet("background-color: green")
main_frame_layout.addWidget(frame_green1, 1, 0)
frame_green1_layout = QVBoxLayout()
frame_green1_layout.setContentsMargins(40, 40, 40, 40)
frame_green1_layout.setSpacing(10)
frame_green1_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
frame_green1.setLayout(frame_green1_layout)
label_1 = QLabel(text="Лейбл 1", parent=frame_green1)
label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_1.setStyleSheet("font-size: 13px; color: black")
label_2 = QLabel(text="Лейбл 2", parent=frame_green1)
label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_2.setStyleSheet("font-size: 13px; color: black")
frame_green1_layout.addWidget(label_1)
frame_green1_layout.addWidget(label_2)

frame_green2 = QFrame(parent=main_frame)
frame_green2.setStyleSheet("background-color: green")
main_frame_layout.addWidget(frame_green2, 1, 1)
frame_green2_layout = QVBoxLayout()
frame_green2_layout.setContentsMargins(40, 40, 40, 40)
frame_green2_layout.setSpacing(10)
frame_green2_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
frame_green2.setLayout(frame_green2_layout)
label_3 = QLabel(text="Лейбл 1", parent=frame_green2)
label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_3.setStyleSheet("font-size: 13px; color: black")
label_4 = QLabel(text="Лейбл 2", parent=frame_green2)
label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_4.setStyleSheet("font-size: 13px; color: black")
frame_green2_layout.addWidget(label_3)
frame_green2_layout.addWidget(label_4)

frame_green3 = QFrame(parent=main_frame)
frame_green3.setStyleSheet("background-color: green")
main_frame_layout.addWidget(frame_green3, 1, 2)
frame_green3_layout = QVBoxLayout()
frame_green3_layout.setContentsMargins(40, 40, 40, 40)
frame_green3_layout.setSpacing(10)
frame_green3_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
frame_green3.setLayout(frame_green3_layout)
label_5 = QLabel(text="Лейбл 1", parent=frame_green3)
label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_5.setStyleSheet("font-size: 13px; color: black")
label_6 = QLabel(text="Лейбл 2", parent=frame_green3)
label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
label_6.setStyleSheet("font-size: 13px; color: black")
frame_green3_layout.addWidget(label_5)
frame_green3_layout.addWidget(label_6)



frame_blue1 = QFrame(parent=main_frame)
frame_blue1.setStyleSheet("background-color: blue")
main_frame_layout.addWidget(frame_blue1, 2, 0)
frame_blue1_layout = QHBoxLayout()
frame_blue1_layout.setContentsMargins(20, 20, 20, 20)
frame_blue1_layout.setSpacing(50)
frame_blue1_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
frame_blue1.setLayout(frame_blue1_layout)

frame_blue1_white1 = QFrame(parent=frame_blue1)
frame_blue1_white1.setStyleSheet("background-color: white")
frame_blue1_white1.setFixedSize(60, 60)
frame_blue1_layout.addWidget(frame_blue1_white1)

frame_blue1_white2 = QFrame(parent=frame_blue1)
frame_blue1_white2.setStyleSheet("background-color: lightgrey")
frame_blue1_white2.setFixedSize(60, 60)
frame_blue1_layout.addWidget(frame_blue1_white2)

frame_blue2 = QFrame(parent=main_frame)
frame_blue2.setStyleSheet("background-color: blue")
main_frame_layout.addWidget(frame_blue2, 2, 1)

frame_blue3 = QFrame(parent=main_frame)
frame_blue3.setStyleSheet("background-color: blue")
main_frame_layout.addWidget(frame_blue3, 2, 2)
frame_blue3_layout = QHBoxLayout()
frame_blue3_layout.setContentsMargins(20, 20, 20, 20)
frame_blue3_layout.setSpacing(50)
frame_blue3_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
frame_blue3.setLayout(frame_blue3_layout)

frame_blue3_white1 = QFrame(parent=frame_blue3)
frame_blue3_white1.setStyleSheet("background-color: white")
frame_blue3_white1.setFixedSize(60, 60)
frame_blue3_layout.addWidget(frame_blue3_white1)

frame_blue3_white2 = QFrame(parent=frame_blue3)
frame_blue3_white2.setStyleSheet("background-color: lightgrey")
frame_blue3_white2.setFixedSize(60, 60)
frame_blue3_layout.addWidget(frame_blue3_white2)



