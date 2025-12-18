'''
ПРИЛОЖЕНИЕ ДЛЯ ПЛАНИРОВАНИЯ ЗАДАЧ
'''
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime


class SimpleTaskApp:

    def __init__(self):
        #СОЗДАЕМ ГЛАВНОЕ ОКНО
        self.window = tk.Tk()
        self.window.title("Мой планировщик")
        self.window.geometry("900x600")
        self.window.minsize(700, 400)  # Минимальный размер

        # Центрируем окно
        self.center_window()

        #НАСТРАИВАЕМ ВНЕШНИЙ ВИД
        self.window.configure(bg="#f0f0f0")  # Светло-серый фон

        #СОЗДАЕМ ПЕРЕМЕННЫЕ
        self.tasks = []  # Список для хранения задач

        #ЗАГРУЖАЕМ СОХРАНЕННЫЕ ЗАДАЧИ
        self.load_tasks()

        #СОЗДАЕМ ИНТЕРФЕЙС
        self.create_widgets()

        #ЗАПУСКАЕМ ПРИЛОЖЕНИЕ
        self.window.mainloop()

    def center_window(self):
        '''Центрируем окно на экране'''
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        '''Создаем все элементы интерфейса'''

        # ЗАГОЛОВОК ПРИЛОЖЕНИЯ
        title_frame = tk.Frame(self.window, bg="#4a86e8")
        title_frame.pack(fill="x", padx=10, pady=10)

        title_label = tk.Label(
            title_frame,
            text="📝 Мой Планировщик Задач",
            font=("Arial", 20, "bold"),
            bg="#4a86e8",
            fg="white"
        )
        title_label.pack(pady=10)

        main_container = tk.Frame(self.window, bg="#f0f0f0")
        main_container.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # ЛЕВАЯ ПАНЕЛЬ - ДОБАВЛЕНИЕ ЗАДАЧ
        left_panel = tk.Frame(main_container, bg="white", relief="solid", bd=1)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 5))

        # Заголовок левой панели
        left_title = tk.Label(
            left_panel,
            text="Добавить новую задачу",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        left_title.pack(pady=10)

        # Поле для названия задачи
        tk.Label(left_panel, text="Название задачи:",
                 bg="white", font=("Arial", 10)).pack(anchor="w", padx=20, pady=(10, 0))

        self.task_name_entry = tk.Entry(left_panel, font=("Arial", 11), width=30)
        self.task_name_entry.pack(fill="x", padx=20, pady=(5, 10))

        # Поле для описания
        tk.Label(left_panel, text="Описание:",
                 bg="white", font=("Arial", 10)).pack(anchor="w", padx=20)

        self.task_desc_text = tk.Text(left_panel, height=4, font=("Arial", 11), width=30)
        self.task_desc_text.pack(fill="x", padx=20, pady=(5, 10))

        # Выбор приоритета
        tk.Label(left_panel, text="Приоритет:",
                 bg="white", font=("Arial", 10)).pack(anchor="w", padx=20)

        self.priority_var = tk.StringVar(value="Средний")
        priority_options = ["Высокий", "Средний", "Низкий"]

        for option in priority_options:
            rb = tk.Radiobutton(
                left_panel,
                text=option,
                variable=self.priority_var,
                value=option,
                bg="white",
                font=("Arial", 10)
            )
            rb.pack(anchor="w", padx=40)

        # Кнопка добавления задачи
        add_button = tk.Button(
            left_panel,
            text="➕ Добавить задачу",
            command=self.add_task,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=8
        )
        add_button.pack(pady=20)

        # ПРАВАЯ ПАНЕЛЬ - СПИСОК ЗАДАЧ
        right_panel = tk.Frame(main_container, bg="white", relief="solid", bd=1)
        right_panel.pack(side="right", fill="both", expand=True, padx=(5, 0))

        # Заголовок правой панели
        right_title = tk.Label(
            right_panel,
            text="Список задач",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        right_title.pack(pady=10)

        # Панель управления
        control_frame = tk.Frame(right_panel, bg="white")
        control_frame.pack(fill="x", padx=20, pady=(0, 10))

        # Кнопки управления
        tk.Button(
            control_frame,
            text="✅ Выполнить",
            command=self.mark_done,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10)
        ).pack(side="left", padx=2)

        tk.Button(
            control_frame,
            text="✏️ Редактировать",
            command=self.edit_task_window,
            bg="#FF9800",
            fg="white",
            font=("Arial", 10)
        ).pack(side="left", padx=2)

        tk.Button(
            control_frame,
            text="🗑️ Удалить",
            command=self.delete_task,
            bg="#F44336",
            fg="white",
            font=("Arial", 10)
        ).pack(side="left", padx=2)

        # Список задач
        list_frame = tk.Frame(right_panel, bg="white")
        list_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.tasks_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 11),
            selectmode="single",
            yscrollcommand=scrollbar.set,
            height=15
        )
        self.tasks_listbox.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.tasks_listbox.yview)

        # Привязываем двойной клик для редактирования
        self.tasks_listbox.bind("<Double-Button-1>", lambda e: self.edit_task_window())

        # Строка состояния
        self.status_label = tk.Label(
            self.window,
            text="Всего задач: 0",
            bg="#e0e0e0",
            font=("Arial", 10),
            anchor="w",
            padx=10
        )
        self.status_label.pack(side="bottom", fill="x", pady=(0, 5))

        # ОБНОВЛЯЕМ СПИСОК ЗАДАЧ
        self.update_task_list()

    def add_task(self):
        """Добавляем новую задачу"""
        # Получаем данные из полей ввода
        name = self.task_name_entry.get().strip()
        description = self.task_desc_text.get("1.0", tk.END).strip()
        priority = self.priority_var.get()

        # Проверяем, что название не пустое
        if not name:
            messagebox.showwarning("Ошибка", "Введите название задачи!")
            return

        # Создаем задачу
        task = {
            "id": len(self.tasks) + 1,
            "name": name,
            "description": description,
            "priority": priority,
            "status": "Активна",
            "created": datetime.now().strftime("%d.%m.%Y %H:%M")
        }

        # Добавляем задачу в список
        self.tasks.append(task)

        # Очищаем поля ввода
        self.task_name_entry.delete(0, tk.END)
        self.task_desc_text.delete("1.0", tk.END)

        # Обновляем список и сохраняем
        self.update_task_list()
        self.save_tasks()

        messagebox.showinfo("Успех", "Задача добавлена!")

    def update_task_list(self):
        '''Обновляем список задач'''
        # Очищаем текущий список
        self.tasks_listbox.delete(0, tk.END)

        # Добавляем задачи
        for task in self.tasks:
            # Определяем символ по статусу
            status_symbol = "✅" if task["status"] == "Выполнена" else "⬜"

            # Определяем цвет по приоритету
            color_tag = ""
            if task["priority"] == "Высокий":
                color_tag = " 🔴"
            elif task["priority"] == "Средний":
                color_tag = " 🟡"
            else:
                color_tag = " 🟢"

            # Формируем строку для отображения
            display_text = f"{status_symbol} {task['name']}{color_tag}"
            self.tasks_listbox.insert(tk.END, display_text)

        # Обновляем строку состояния
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task["status"] == "Выполнена")
        self.status_label.config(text=f"Всего задач: {total} | Выполнено: {done}")

    def mark_done(self):
        '''Отмечаем задачу как выполненную'''
        # Получаем выбранную задачу
        selected_index = self.tasks_listbox.curselection()

        if not selected_index:
            messagebox.showwarning("Ошибка", "Выберите задачу!")
            return

        # Получаем индекс выбранной задачи
        index = selected_index[0]

        # Меняем статус
        if self.tasks[index]["status"] == "Активна":
            self.tasks[index]["status"] = "Выполнена"
            messagebox.showinfo("Успех", "Задача отмечена как выполненная!")
        else:
            self.tasks[index]["status"] = "Активна"
            messagebox.showinfo("Успех", "Задача возвращена в активные!")

        # Обновляем список и сохраняем
        self.update_task_list()
        self.save_tasks()

    def delete_task(self):
        '''Удаляем задачу'''
        # Получаем выбранную задачу
        selected_index = self.tasks_listbox.curselection()

        if not selected_index:
            messagebox.showwarning("Ошибка", "Выберите задачу!")
            return

        # Подтверждаем удаление
        if not messagebox.askyesno("Подтверждение", "Удалить выбранную задачу?"):
            return

        # Удаляем задачу
        index = selected_index[0]
        del self.tasks[index]

        # Обновляем ID оставшихся задач
        for i, task in enumerate(self.tasks, 1):
            task["id"] = i

        # Обновляем список и сохраняем
        self.update_task_list()
        self.save_tasks()

        messagebox.showinfo("Успех", "Задача удалена!")

    def edit_task_window(self):
        '''Открываем окно для редактирования задачи'''
        # Получаем выбранную задачу
        selected_index = self.tasks_listbox.curselection()

        if not selected_index:
            messagebox.showwarning("Ошибка", "Выберите задачу для редактирования!")
            return

        index = selected_index[0]
        task = self.tasks[index]

        # СОЗДАЕМ ОКНО РЕДАКТИРОВАНИЯ
        edit_window = tk.Toplevel(self.window)
        edit_window.title("Редактировать задачу")
        edit_window.geometry("400x350")
        edit_window.configure(bg="#f0f0f0")
        edit_window.transient(self.window)  # Связываем с главным окном
        edit_window.grab_set()  # Блокируем главное окно

        # Центрируем окно редактирования
        edit_window.update_idletasks()
        x = self.window.winfo_x() + 50
        y = self.window.winfo_y() + 50
        edit_window.geometry(f"+{x}+{y}")

        # Заголовок окна
        tk.Label(
            edit_window,
            text="Редактировать задачу",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0"
        ).pack(pady=10)

        # Поле для названия
        tk.Label(edit_window, text="Название:",
                 bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w", padx=20)

        name_entry = tk.Entry(edit_window, font=("Arial", 11), width=30)
        name_entry.insert(0, task["name"])
        name_entry.pack(fill="x", padx=20, pady=(5, 10))

        # Поле для описания
        tk.Label(edit_window, text="Описание:",
                 bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w", padx=20)

        desc_text = tk.Text(edit_window, height=4, font=("Arial", 11), width=30)
        desc_text.insert("1.0", task["description"])
        desc_text.pack(fill="x", padx=20, pady=(5, 10))

        # Выбор приоритета
        tk.Label(edit_window, text="Приоритет:",
                 bg="#f0f0f0", font=("Arial", 10)).pack(anchor="w", padx=20)

        priority_var = tk.StringVar(value=task["priority"])
        priority_options = ["Высокий", "Средний", "Низкий"]

        for option in priority_options:
            rb = tk.Radiobutton(
                edit_window,
                text=option,
                variable=priority_var,
                value=option,
                bg="#f0f0f0",
                font=("Arial", 10)
            )
            rb.pack(anchor="w", padx=40)

        # Фрейм для кнопок
        button_frame = tk.Frame(edit_window, bg="#f0f0f0")
        button_frame.pack(pady=20)

        # Кнопка сохранения
        def save_changes():
            task["name"] = name_entry.get().strip()
            task["description"] = desc_text.get("1.0", tk.END).strip()
            task["priority"] = priority_var.get()

            if not task["name"]:
                messagebox.showwarning("Ошибка", "Название не может быть пустым!")
                return

            self.update_task_list()
            self.save_tasks()
            edit_window.destroy()
            messagebox.showinfo("Успех", "Задача обновлена!")

        tk.Button(
            button_frame,
            text="💾 Сохранить",
            command=save_changes,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5
        ).pack(side="left", padx=5)

        # Кнопка отмены
        tk.Button(
            button_frame,
            text="❌ Отмена",
            command=edit_window.destroy,
            bg="#F44336",
            fg="white",
            font=("Arial", 10),
            padx=15,
            pady=5
        ).pack(side="left", padx=5)

    def show_statistics_window(self):
        '''Показываем окно статистики'''
        # Создаем окно статистики
        stats_window = tk.Toplevel(self.window)
        stats_window.title("Статистика")
        stats_window.geometry("300x250")
        stats_window.configure(bg="#f0f0f0")

        # Центрируем
        stats_window.update_idletasks()
        x = self.window.winfo_x() + 100
        y = self.window.winfo_y() + 100
        stats_window.geometry(f"+{x}+{y}")

        # Заголовок
        tk.Label(
            stats_window,
            text="📊 Статистика задач",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0"
        ).pack(pady=15)

        # Считаем статистику
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task["status"] == "Выполнена")
        active = total - done

        high = sum(1 for task in self.tasks if task["priority"] == "Высокий")
        medium = sum(1 for task in self.tasks if task["priority"] == "Средний")
        low = sum(1 for task in self.tasks if task["priority"] == "Низкий")

        # Показываем статистику
        tk.Label(
            stats_window,
            text=f"Всего задач: {total}",
            bg="#f0f0f0",
            font=("Arial", 11)
        ).pack(pady=5)

        tk.Label(
            stats_window,
            text=f"Выполнено: {done}",
            bg="#f0f0f0",
            font=("Arial", 11)
        ).pack(pady=5)

        tk.Label(
            stats_window,
            text=f"Активных: {active}",
            bg="#f0f0f0",
            font=("Arial", 11)
        ).pack(pady=5)

        # Разделитель
        tk.Frame(stats_window, height=2, bg="gray").pack(fill="x", padx=20, pady=10)

        tk.Label(
            stats_window,
            text="По приоритетам:",
            bg="#f0f0f0",
            font=("Arial", 11, "bold")
        ).pack(pady=5)

        tk.Label(
            stats_window,
            text=f"Высокий: {high}  Средний: {medium}  Низкий: {low}",
            bg="#f0f0f0",
            font=("Arial", 10)
        ).pack(pady=5)

        # Кнопка закрытия
        tk.Button(
            stats_window,
            text="Закрыть",
            command=stats_window.destroy,
            bg="#4a86e8",
            fg="white",
            font=("Arial", 10),
            padx=20,
            pady=5
        ).pack(pady=20)

    def save_tasks(self):
        """Сохраняем задачи в файл"""
        try:
            with open("tasks.json", "w", encoding="utf-8") as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Ошибка сохранения: {e}")

    def load_tasks(self):
        """Загружаем задачи из файла"""
        try:
            if os.path.exists("tasks.json"):
                with open("tasks.json", "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            self.tasks = []


# ЗАПУСК ПРИЛОЖЕНИЯ
if __name__ == "__main__":
    app = SimpleTaskApp()
