# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2026-02-02 13:52:00
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2026-02-02 14:23:39

import flet as ft
import asyncio


class savefile(ft.Button):
    def __init__(self):
        super().__init__()
        self.icon = ft.Icons.SAVE
        self.content = "save"
        self.on_click = self.handle_click

    async def handle_click(self):
        content = """
    The bug in the Android version of Filepicker has been reproduced.
This will demonstrate how to save a file.
And successfully reproduce the bug. 

    filepicker 安卓版 bug 复现.
这里将演示如何保存一个文件.
并成功复刻出bug.

    Android版Filepickerのバグ再現。ファイルの保存方法を説明します。
バグは再現されました。

    The text above will be saved to a file, 
with the goal of making it work on all platforms.
"""
        content_bytes = content.encode("utf-8")
        is_mobile_or_web = self.page.web or self.page.platform in [
            ft.PagePlatform.ANDROID,
            ft.PagePlatform.IOS,
        ]
        save_path = await ft.FilePicker().save_file(
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["text"],
            file_name="content_bytes.text",
            src_bytes=content_bytes,
        )
        if save_path and not is_mobile_or_web:
            with open(save_path, "wb") as f:
                f.write(content_bytes)
            print("Desktop file save complete. [ linux windows and macos ]")


def main(page: ft.Page):
    _savefile = savefile()
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=ft.Row(
                    expand=1,
                    scroll=ft.ScrollMode.HIDDEN,
                    spacing=10,
                    controls=[_savefile],
                ),
                alignment=ft.Alignment.CENTER,
            ),
        )
    )
    page.update()


ft.run(main)
