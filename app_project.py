import json
import os

FILE_NAME = 'projects.json'

def load_projects():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_projects(projects):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        # indent=2 делает JSON красивым и читаемым
        json.dump(projects, f, ensure_ascii=False, indent=2)

def main():
    print("=== Добавление нового проекта на сайт ===")
    title = input("Название проекта (например, MyNewApp): ")
    description = input("Краткое описание: ")
    url = input("Ссылка (например, /mynewapp или https://...): ")

    new_project = {
        "title": title,
        "description": description,
        "url": url
    }

    projects = load_projects()
    projects.append(new_project)
    save_projects(projects)

    print(f"\n✅ Проект '{title}' успешно добавлен в {FILE_NAME}!")
    print("Осталось сделать git commit и git push!")

if __name__ == '__main__':
    main()