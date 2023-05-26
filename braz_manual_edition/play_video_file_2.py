import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFileDialog, QPushButton
from PySide2.QtMultimedia import QMediaPlayer
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtCore import QUrl, Qt

class VideoPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 800, 600)

        # Erstellen des Videowiedergabe-Widgets
        self.video_widget = QVideoWidget()

        # Erstellen des Media Players
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        # Layout erstellen und das Video-Wiedergabe-Widget hinzufügen
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)

        # Steuerungsbuttons erstellen
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")
        self.seek_forward_button = QPushButton("Seek Forward")
        self.seek_backward_button = QPushButton("Seek Backward")

        # Signal-Slot-Verbindungen für die Steuerungsbuttons
        self.play_button.clicked.connect(self.media_player.play)
        self.pause_button.clicked.connect(self.media_player.pause)
        self.stop_button.clicked.connect(self.media_player.stop)
        self.seek_forward_button.clicked.connect(self.seek_forward)
        self.seek_backward_button.clicked.connect(self.seek_backward)

        # Steuerungsbuttons dem Layout hinzufügen
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.seek_forward_button)
        layout.addWidget(self.seek_backward_button)

        # Hauptwidget erstellen und das Layout setzen
        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)

        # Öffnen einer Videodatei beim Start des Players
        self.open_file()

    def open_file(self):
        # Dialog zum Auswählen einer Videodatei anzeigen
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Video auswählen", "", "Video Files (*.mp4 *.mkv)")

        # Wenn eine Datei ausgewählt wurde, Videodatei abspielen
        if file_path:
            video_url = QUrl.fromLocalFile(file_path)
            self.media_player.setMedia(video_url)
            self.media_player.play()

    def seek_forward(self):
        # Video um 5 Sekunden vorwärts spulen
        current_position = self.media_player.position()
        new_position = current_position + 5000  # 5000 Millisekunden (5 Sekunden)
        self.media_player.setPosition(new_position)

    def seek_backward(self):
        # Video um 5 Sekunden rückwärts spulen
        current_position = self.media_player.position()
        new_position = current_position - 5000  # 5000 Millisekunden (5 Sekunden)
        if new_position < 0:
            new_position = 0
        self.media_player.setPosition(new_position)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player_window = VideoPlayerWindow()
    player_window.show()
    sys.exit(app.exec_())
