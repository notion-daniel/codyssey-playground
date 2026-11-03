# attend.py - 스터디 출석부 프로그램
# 외부 라이브러리 없이 표준 라이브러리만 사용

import os
from datetime import date

FILE_NAME = "attendance.txt"  # 출석 기록을 저장할 파일


# ── 출석 추가 ──────────────────────────────────────────────
def add_attendance():
    today = date.today().strftime("%Y-%m-%d")  # 오늘 날짜 자동 생성
    print(f"  오늘 날짜: {today}")

    # 날짜 직접 입력하거나 엔터만 누르면 오늘 날짜 사용
    date_input = input("  날짜 입력 (그냥 엔터 = 오늘): ").strip()
    if date_input == "":
        date_input = today

    name = input("  이름 입력: ").strip()
    if name == "":
        print("  ⚠️  이름을 입력해야 합니다.")
        return

    # 파일에 이어쓰기 (a 모드)
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{date_input},{name}\n")

    print(f"  ✅ {date_input} | {name} 출석 완료!\n")


# ── 출석 목록 보기 ─────────────────────────────────────────
def show_attendance():
    if not os.path.exists(FILE_NAME):
        print("  아직 출석 기록이 없습니다.\n")
        return

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]  # 빈 줄 제거

    if not lines:
        print("  아직 출석 기록이 없습니다.\n")
        return

    print()
    print("  ┌─────────────────────────────┐")
    print("  │        📋 출석 목록          │")
    print("  ├──────────────┬──────────────┤")
    print("  │     날짜     │     이름     │")
    print("  ├──────────────┼──────────────┤")

    for line in lines:
        parts = line.split(",", 1)           # 날짜,이름 으로 나누기
        if len(parts) == 2:
            d, n = parts[0].strip(), parts[1].strip()
            print(f"  │ {d:<12} │ {n:<12} │")
        else:
            print(f"  │ {line:<27} │")       # 형식이 깨진 줄은 그냥 출력

    print("  └──────────────┴──────────────┘")
    print(f"  총 {len(lines)}건\n")


# ── 메인 메뉴 ──────────────────────────────────────────────
def main():
    print("=" * 35)
    print("     📖 스터디 출석부")
    print("=" * 35)

    while True:
        print("  1. 출석 추가")
        print("  2. 목록 보기")
        print("  3. 종료")
        choice = input("  번호 선택: ").strip()

        if choice == "1":
            add_attendance()
        elif choice == "2":
            show_attendance()
        elif choice == "3":
            print("  👋 프로그램을 종료합니다.")
            break
        else:
            print("  ⚠️  1, 2, 3 중에서 선택하세요.\n")


if __name__ == "__main__":
    main()