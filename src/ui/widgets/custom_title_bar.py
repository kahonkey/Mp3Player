# class CustomTitleBar(QWidget):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.setAutoFillBackground(True)
#         self.setBackgroundRole(QPalette.ColorRole.Highlight)
#         self.initial_pos = None
#         title_bar_layout = QHBoxLayout(self)
#         title_bar_layout.setContentsMargins(0, 0, 0, 0)
#         title_bar_layout.setSpacing(0)
#         title_bar_layout.setVerticalSizeConstraint(QHBoxLayout.SizeConstraint.SetMaximumSize)
#
#         self.title = QLabel(f"{self.__class__.__name__}", self)
#         self.title.setStyleSheet("font-size: 9px")
#         self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         if title := parent.windowTitle():
#             self.title.setText(title)
#         title_bar_layout.addWidget(self.title)
#         # Min button
#         self.min_button = QToolButton(self)
#         min_icon = self.style().standardIcon(
#             QStyle.StandardPixmap.SP_TitleBarMinButton
#         )
#         self.min_button.setIcon(min_icon)
#         self.min_button.clicked.connect(self.window().showMinimized)
#
#         # Max button
#         self.max_button = QToolButton(self)
#         max_icon = self.style().standardIcon(
#             QStyle.StandardPixmap.SP_TitleBarMaxButton
#         )
#         self.max_button.setIcon(max_icon)
#         self.max_button.clicked.connect(self.window().showMaximized)
#
#         # Close button
#         self.close_button = QToolButton(self)
#         close_icon = self.style().standardIcon(
#             QStyle.StandardPixmap.SP_TitleBarCloseButton
#         )
#         self.close_button.setIcon(close_icon)
#         self.close_button.clicked.connect(self.window().close)
#
#         # Normal button
#         self.normal_button = QToolButton(self)
#         normal_icon = self.style().standardIcon(
#             QStyle.StandardPixmap.SP_TitleBarNormalButton
#         )
#         self.normal_button.setIcon(normal_icon)
#         self.normal_button.clicked.connect(self.window().showNormal)
#         self.normal_button.setVisible(False)
#         # Add buttons
#         buttons = [
#             self.min_button,
#             self.normal_button,
#             self.max_button,
#             self.close_button,
#         ]
#         for button in buttons:
#             button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
#             button.setFixedSize(QSize(11, 11))
#             #button.setStyleSheet()
#             title_bar_layout.addWidget(button)
#
#     def window_state_changed(self, state):
#         if state == Qt.WindowState.WindowMaximized:
#             self.normal_button.setVisible(True)
#             self.max_button.setVisible(False)
#         else:
#             self.normal_button.setVisible(False)
#             self.max_button.setVisible(True)

# from PySide6.QtCore import QFileSystemWatcher
# 
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.watcher = QFileSystemWatcher(["styles.qss"])
#         self.watcher.fileChanged.connect(self.load_styles)
#         self.load_styles()
# 
#     def load_styles(self):
#         with open("styles.qss", "r") as f:
#             self.setStyleSheet(f.read())
#         print("QSS reloaded")
