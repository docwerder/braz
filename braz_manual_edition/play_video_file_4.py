import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QListWidget
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

        # Steuerungsbuttons erstellen
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")

        # Signal-Slot-Verbindungen für die Steuerungsbuttons
        self.play_button.clicked.connect(self.media_player.play)
        self.pause_button.clicked.connect(self.media_player.pause)
        self.stop_button.clicked.connect(self.media_player.stop)

        # Layout erstellen und die Widgets hinzufügen
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

    def open_file(self):
        # Dialog zum Auswählen einer Videodatei anzeigen
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Video auswählen", "", "Video Files (*.mp4 *.mkv)")

        # Wenn eine Datei ausgewählt wurde, Videodatei abspielen
        if file_path:
            video_url = QUrl.fromLocalFile(file_path)
            self.media_player.setMedia(video_url)
            self.media_player.play()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # QLabel erstellen
        label = QLabel("Dies ist ein QLabel.")

        # VideoPlayerWidget erstellen
        video_player = VideoPlayerWidget()

        # Layout erstellen und QLabel sowie VideoPlayerWidget hinzufügen
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(video_player)
        self.setLayout(layout)

        # Video im VideoPlayerWidget öffnen
        video_player.open_file()

        # Steuerungsbuttons des VideoPlayerWidgets hinzufügen
        layout.addWidget(video_player.play_button)
        layout.addWidget(video_player.pause_button)
        layout.addWidget(video_player.stop_button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
