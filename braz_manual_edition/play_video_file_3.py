import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide2.QtMultimedia import QMediaPlayer
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtCore import QUrl

class VideoPlayerWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Erstellen des Videowiedergabe-Widgets
        self.video_widget = QVideoWidget()

        # Erstellen des Media Players
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        # Layout erstellen und das Video-Wiedergabe-Widget hinzufügen
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        self.setLayout(layout)

    def open_file(self, file_path):
        # Videodatei abspielen
        video_url = QUrl.fromLocalFile(file_path)
        self.media_player.setMedia(video_url)
        self.media_player.play()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("External Program")
        self.setGeometry(100, 100, 800, 600)

        # QLabel erstellen
        label = QLabel("Dies ist ein QLabel.")

        # VideoPlayerWidget erstellen
        video_player = VideoPlayerWidget()

        # Layout erstellen und QLabel sowie VideoPlayerWidget hinzufügen
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(video_player)

        # Hauptwidget erstellen und das Layout setzen
        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)

        # Video im VideoPlayerWidget öffnen
        video_player.open_file("/Users/joerg/Downloads/closing-costs_1080p.mp4")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
