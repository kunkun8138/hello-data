"""hello-data: 第一个项目，用来验证 Python 环境是否跑通。"""

from datetime import datetime


def average(values: list[float]) -> float:
    """计算平均值。"""
    if not values:
        raise ValueError("values 不能为空")
    return sum(values) / len(values)


def main() -> None:
    temps = [21.5, 22.0, 19.8, 23.1, 20.4]
    print(f"样本数: {len(temps)}")
    print(f"平均气温: {average(temps):.2f} °C")
    print(f"运行时间: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print("环境验证通过 ✅")


if __name__ == "__main__":
    main()
