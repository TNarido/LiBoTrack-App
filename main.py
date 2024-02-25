from flet import *
from components.Library import Library

def main(page: Page):
    page.title = "LiBoTrack"
    page.window_maximized = True
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }
    page.update()

    #++++++++++++++++++++++++++++++++++++BAR-CHART--ALERT-DIALOG--DEFINED-FUNCTIONS++++++++++++++++++++++++++++++++++++#

    def close_barchart(e):
        alertbarchart.open = False
        page.update()

    def open_barchart(e):
        page.dialog = alertbarchart
        alertbarchart.open = True
        page.update()

    #++++++++++++++++++++++++++++++++++++SHELF / IMAGES--ALERT-DIALOG--DEFINED-FUNCTIONS++++++++++++++++++++++++++++++++++++#

    def close_shelf(e):
        alertshelf.open = False
        page.update()

    def open_shelf(e):
        page.dialog = alertshelf
        alertshelf.open = True
        page.update()

    #++++++++++++++++++++++++++++++++++++NAVIGATION-BAR++++++++++++++++++++++++++++++++++++#

    NavBar = AppBar(
            leading_width = 70,
            toolbar_height = 70,
            title = Text("Library Book Tracker App", font_family = "Times New Roman", weight = FontWeight.BOLD, size = 40),
            center_title = False,
            bgcolor = colors.BLUE_GREY_300,
            actions = [
                IconButton(icons.BOOK, on_click = open_shelf),
                VerticalDivider(width = 10, color = colors.BLUE_GREY_300),
                IconButton(icons.BAR_CHART, on_click = open_barchart),
                VerticalDivider(width = 15, color = colors.BLUE_GREY_300)
            ]
        )
    
    #++++++++++++++++++++++++++++++++++++BAR-CHART++++++++++++++++++++++++++++++++++++#

    barchart = BarChart(
        bar_groups = [
            BarChartGroup(
                x = 0,
                bar_rods = [
                    BarChartRod(
                        from_y = 0,
                        to_y = 20,
                        width = 90,
                        color = colors.BLUE,
                        tooltip = "Borrowed",
                        border_radius = 10,
                    ),
                    BarChartRod(
                        from_y = 0,
                        to_y = 20,
                        width = 90,
                        color = colors.BLUE_200,
                        tooltip = "Returned",
                        border_radius = 10,
                    ),
                ]
            ),
            BarChartGroup(
                x = 1,
                bar_rods = [
                    BarChartRod(
                        from_y = 0,
                        to_y = 15,
                        width = 90,
                        color = colors.GREEN,
                        tooltip = "Borrowed",
                        border_radius = 10,
                    ),
                    BarChartRod(
                        from_y = 0,
                        to_y = 13,
                        width = 90,
                        color = colors.GREEN_200,
                        tooltip = "Returned",
                        border_radius = 10,
                    ),
                ]
            ),
            BarChartGroup(
                x = 2,
                bar_rods = [
                    BarChartRod(
                        from_y = 0,
                        to_y = 10,
                        width = 90,
                        color = colors.RED,
                        tooltip = "Borrowed",
                        border_radius = 10,
                    ),
                    BarChartRod(
                        from_y = 0,
                        to_y = 10,
                        width = 90,
                        color = colors.RED_200,
                        tooltip = "Returned",
                        border_radius = 10,
                    ),
                ]
            ),
            BarChartGroup(
                x = 3,
                bar_rods = [
                    BarChartRod(
                        from_y = 0,
                        to_y = 25,
                        width = 90,
                        color = colors.YELLOW,
                        tooltip = "Borrowed",
                        border_radius = 10,
                    ),
                    BarChartRod(
                        from_y = 0,
                        to_y = 28,
                        width = 90,
                        color = colors.YELLOW_200,
                        tooltip = "Returned",
                        border_radius = 10,
                    ),
                ]
            ),
            BarChartGroup(
                x = 4,
                bar_rods = [
                    BarChartRod(
                        from_y = 0,
                        to_y = 5,
                        width = 90,
                        color = colors.PINK,
                        tooltip = "Borrowed",
                        border_radius = 10,
                    ),
                    BarChartRod(
                        from_y = 0,
                        to_y = 5,
                        width = 90,
                        color = colors.PINK_200,
                        tooltip = "Returned",
                        border_radius = 10,
                    ),
                ]
            )
        ],
        border = border.all(1 ,colors.BLACK),
        left_axis = ChartAxis(
            labels_size = 40,
            title = Text("No. of Students", weight = FontWeight.BOLD, size = 25, font_family = "Times New Roman"),
            title_size = 30,
            labels_interval = 5
        ),
        bottom_axis = ChartAxis(
            title = Text("Weekdays", weight = FontWeight.BOLD, size = 30, text_align = "center", font_family = "Times New Roman"), 
            title_size = 40,
            labels_size = 45,
            labels = [
                ChartAxisLabel(
                    value = 0,
                    label = Container(Text("Monday", weight = FontWeight.BOLD, font_family = "Times New Roman"), padding = 10)
                ),
                ChartAxisLabel(
                    value = 1,
                    label = Container(Text("Tuesday", weight = FontWeight.BOLD, font_family = "Times New Roman"), padding = 10)
                ),
                ChartAxisLabel(
                    value = 2,
                    label = Container(Text("Wednesday", weight = FontWeight.BOLD, font_family = "Times New Roman"), padding = 10)
                ),
                ChartAxisLabel(
                    value = 3,
                    label = Container(Text("Thursday", weight = FontWeight.BOLD, font_family = "Times New Roman"), padding = 10)
                ),
                ChartAxisLabel(
                    value = 4,
                    label = Container(Text("Friday", weight = FontWeight.BOLD, font_family = "Times New Roman"), padding = 10)
                )
            ]
        ),
        top_axis = ChartAxis(
            labels_size = 40,
            title = Text("Bar Chart of Borrowed Books", weight = FontWeight.BOLD, size = 28, font_family = "Times New Roman"),
            title_size = 50,
            show_labels = False
        ),
        horizontal_grid_lines = ChartGridLines(
            color = colors.BLUE_GREY_700,
            width = 1,
            dash_pattern = [3, 3],
        ),
        tooltip_bgcolor = colors.with_opacity(0.5, colors.WHITE),
        max_y = 30,
        height = 700,
        width = 1400,
        interactive = True,
        expand = True
    )

    #++++++++++++++++++++++++++++++++++++BOOKS / IMAGES++++++++++++++++++++++++++++++++++++#

    #-----------------------FILE-PICKER--DEFINED-FUNCTIONS-----------------------#

    def on_dialog_result(e : FilePickerResultEvent):
        print("Selected files", e.files)
        print("Selected files or folder", e.path)

    def upload_files(e):
        upload_list = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                upload_list.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url = page.get_upload_url(f.name, 600)
                    )
                )
            file_picker.upload(upload_list)

    #-----------------------FILE-PICKER-----------------------#

    file_picker = FilePicker(on_result = on_dialog_result)
    page.overlay.append(file_picker)

    #-----------------------VARIABLES-----------------------#

    txt = Text(value = "")
    btn = ElevatedButton("Choose files..", icon = icons.FOLDER_OPEN_ROUNDED,
                         on_click = lambda _: file_picker.pick_files(allow_multiple = True), height = 40, color = colors.BLACK)
    btn1 = ElevatedButton("Upload", icon = icons.ARROW_DROP_UP, on_click = upload_files, height = 40, color = colors.BLACK)

    #-----------------------BUTTONS-----------------------#

    buttons = Row(controls = [
        btn, btn1
    ], alignment = MainAxisAlignment.END)

    #-----------------------TEXT-IN-ROW-----------------------#

    all_txt = Row([
        Text("All", size = 25, weight = FontWeight.BOLD, font_family = "Times New Roman")
        ], alignment = MainAxisAlignment.START
    )

    borrowed_txt = Row([
        Text("Borrowed", size = 25, weight = FontWeight.BOLD, font_family = "Times New Roman")
        ], alignment = MainAxisAlignment.START
    )

    #-----------------------IMAGES-----------------------#

    all_books = Column(expand = 1, wrap = True, scroll = "always")
    for i in range(1, 32):
        all_books.controls.append(
            Image(
                src = f"./books/{i}.jpg",
                width = 200,
                height = 400,
                repeat = ImageRepeat.NO_REPEAT,
            )
        )
    
    borrowed_books = Column(expand = 1, wrap = True, scroll = "always")
    for i in range(20, 29):
        borrowed_books.controls.append(
            Image(
                src = f"./books/{i}.jpg",
                width = 200,
                height = 400,
                repeat = ImageRepeat.NO_REPEAT,
            )
        )

    #-----------------------DISPLAYED-BOOKS-----------------------#

    books = Container(
        content = Column(controls=[
            Text("Books", size = 50, weight = FontWeight.BOLD, width = 200, font_family = "Times New Roman"),
            buttons,
            Divider(height = 4, color = colors.BLACK),
            all_txt,
            all_books,
            Divider(height = 4, color = colors.BLACK),
            borrowed_txt,
            borrowed_books,
            txt,
        ], horizontal_alignment = CrossAxisAlignment.CENTER, spacing = 20),
        padding = 5,
        alignment = alignment.top_center,
        height = 900,
        width = 9000,
    )

    #++++++++++++++++++++++++++++++++++++BAR-CHART--ALERT-DIALOG++++++++++++++++++++++++++++++++++++#

    alertbarchart = AlertDialog(
        modal = True,
        actions = [
            TextButton("Close", on_click = close_barchart)
        ],
        content = (barchart),
        actions_alignment = MainAxisAlignment.END
    )

    #++++++++++++++++++++++++++++++++++++BOOKS--ALERT-DIALOG++++++++++++++++++++++++++++++++++++#

    alertshelf = AlertDialog(
        modal = True,
        actions = [
            TextButton("Close", on_click = close_shelf)
        ],
        content = (
            Column(
                controls = [books], scroll = True
            )
        ),
        actions_alignment = MainAxisAlignment.END
    )

    page.add(
        NavBar,
        Library()
        )

app(target = main, upload_dir = "books")