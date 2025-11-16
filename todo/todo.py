import flet as ft

def main(page: ft.Page):
    page.title = "ToDo アプリ"
    page.scroll = ft.ScrollMode.AUTO

    tasks = []

    def add_task(e):
        task_text = task_input.value.strip()
        if task_text == "":
            return
        task = ft.Checkbox(label=task_text, on_change=toggle_task)
        tasks.append(task)
        task_list.controls.append(ft.Row([task, delete_button(task)]))
        task_input.value = ""
        page.update()

    def delete_button(task):
        return ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=lambda e: delete_task(task)
        )

    def delete_task(task):
        for i, t in enumerate(tasks):
            if t == task:
                tasks.pop(i)
                task_list.controls.pop(i)
                break
        page.update()

    def toggle_task(e):
        # チェックボックスの状態変化時の動作（例: スタイル変更など）
        e.control.label = f"✔️ {e.control.label}" if e.control.value else e.control.label.replace("✔️ ", "")
        page.update()

    task_input = ft.TextField(label="タスクを入力", expand=True, on_submit=add_task)
    add_button = ft.IconButton(icon=ft.icons.ADD, on_click=add_task)

    task_list = ft.Column()

    page.add(
        ft.Row([task_input, add_button]),
        ft.Container(content=task_list, margin=10)
    )

ft.app(target=main)