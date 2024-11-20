from nicegui import ui

def run_code():
    code = input_box.value
    try:
        # 입력된 Python 코드를 실행
        exec_globals = {}
        exec(code, exec_globals)
        output_label.text = str(exec_globals.get('result', '코드 실행 완료!'))
    except Exception as e:
        output_label.text = f"에러 발생: {e}"

# 입력 박스와 실행 버튼 생성
with ui.column():
    ui.label('실행할 Python 코드를 입력하세요:')
    input_box = ui.textarea(placeholder='예: result = 2 + 2') #, rows=5)
    ui.button('코드 실행', on_click=run_code)
    output_label = ui.label('결과가 여기에 표시됩니다.')

ui.run()