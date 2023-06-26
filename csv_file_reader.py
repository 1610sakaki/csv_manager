import csv

# ファイルを読み込み・書き込みを行うクラス
class CSVFileManager:
    def __init__(self) -> None:
        pass

    def read_one_line(self, file_path):
        while True:
            try:
                # startもしくは pause
                with open(file_path, "r", newline="") as operation_file:
                    reader = csv.reader(operation_file)
                    file_header = next(reader)  # 一行目を取得
                    break
            except StopIteration:
                pass
            except FileNotFoundError or FileExistsError:
                print("Not found csv file ")
            except Exception as e:
                print("some csv file error", str(e))

        return file_header

    def write_one_line(self, file_path, option, data):
        while True:
            try:
                with open(file_path, option, newline="") as operation_file:
                    writer = csv.writer(operation_file)
                    if not isinstance(data, list):
                        writer.writerow([data])
                    else:
                        writer.writerow(data)
                    break
            except (FileNotFoundError, FileExistsError):
                print("Not found or existing csv file.")
            except Exception as e:
                print("An error occurred:", str(e))


