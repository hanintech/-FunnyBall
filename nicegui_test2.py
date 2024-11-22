from nicegui import ui

# 학생 데이터를 저장할 리스트
students = []

def add_student(name, score):
    """학생 추가"""
    students.append({'name': name, 'score': score})
    refresh_table()

def refresh_table():
    """학생 목록 새로고침"""
    table.rows.clear()
    for student in students:
        table.add_row(student['name'], student['score'])

def clear_form():
    """입력 폼 초기화"""
    name_input.value = ""
    score_input.value = ""

# 제목
ui.label('성적 관리 시스템').classes('text-2xl text-center my-4')

# 입력 폼
with ui.row():
    name_input = ui.input('학생 이름').classes('w-1/2')
    score_input = ui.number('점수').classes('w-1/4').props('min=0 max=100')
    ui.button('추가', on_click=lambda: add_student(name_input.value, score_input.value)).classes('w-1/4')

# 학생 목록 표시 테이블
table = ui.table().classes('my-4')
table.add_column('이름')
table.add_column('점수')

# 전체 초기화 버튼
ui.button('초기화', on_click=lambda: (students.clear(), refresh_table(), clear_form())).classes('my-4')

# 애플리케이션 실행
ui.run()
