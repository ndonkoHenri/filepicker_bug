# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2026-02-03 04:18:31
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2026-02-03 14:07:01
import traceback
import flet as ft

import sys


def main(page: ft.Page):
    async def handle_pick_files(e: ft.Event[ft.Button]):
        try:
            files = await ft.FilePicker().pick_files(allow_multiple=True)
            selected_files.value = (
                ", ".join(map(lambda f: f.name, files)) if files else "Cancelled!"
            )
        except Exception:
            traceback.print_exc()
            sys.exit(100)

    async def handle_save_file(e: ft.Event[ft.Button]):
        try:
            save_file_path.value = await ft.FilePicker().save_file()
        except Exception:
            traceback.print_exc()
            sys.exit(100)

    async def handle_get_directory_path(e: ft.Event[ft.Button]):
        try:
            directory_path.value = await ft.FilePicker().get_directory_path()
        except Exception:
            traceback.print_exc()
            sys.exit(100)

    page.add(
        ft.Row(
            controls=[
                ft.Button(
                    content="Pick files",
                    icon=ft.Icons.UPLOAD_FILE,
                    on_click=handle_pick_files,
                ),
                selected_files := ft.Text(),
            ]
        ),
        ft.Row(
            controls=[
                ft.Button(
                    content="Save file",
                    icon=ft.Icons.SAVE,
                    on_click=handle_save_file,
                    disabled=page.web,  # disable this button in web mode
                ),
                save_file_path := ft.Text(),
            ]
        ),
        ft.Row(
            controls=[
                ft.Button(
                    content="Open directory",
                    icon=ft.Icons.FOLDER_OPEN,
                    on_click=handle_get_directory_path,
                    disabled=page.web,  # disable this button in web mode
                ),
                directory_path := ft.Text(),
            ]
        ),
    )


ft.run(main)
