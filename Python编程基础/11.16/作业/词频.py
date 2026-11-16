shuru=input("请输入：")

shuru=shuru.lower()
words_list=shuru.split()

word_counts={}

for word in words_list:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\n---词频统计结果---")
for word,count in word_counts.items():
    print(f"单词：{word:<15} 出现次数：{count}")


    
# 进阶
"""
import re
import os
import json
import glob
from typing import List, Dict, Generator, Set
from collections import Counter

# ================= 全局配置区 =================
DEFAULT_STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "is", "are", "was", "were", 
    "in", "on", "at", "to", "of", "for", "it", "this", "that",
    "的", "了", "是", "在", "和", "就", "都", "而", "及", "与", "这", "那"
}
SUPPORTED_ENCODINGS = ['utf-8', 'gbk', 'gb2312', 'latin-1']
ALLOWED_EXTENSIONS = ('.txt', '.log', '.csv', '.md')
CONSOLE_OUTPUT_LIMIT = 15

# 【优化】长正则表达式换行书写，提升可读性
REGEX_WORDS = re.compile(
    r"[a-z]+(?:[-'][a-z]+)*"  # 英文单词或带连字符/撇号的组合
    r"|\d+"                   # 数字
    r"|[\u4e00-\u9fa5]+",     # 中文
    re.IGNORECASE             # 初始编译时忽略大小写，后续逻辑再控制
)
REGEX_EN_NUM = re.compile(r"[a-z]+(?:[-'][a-z]+)*|\d+", re.IGNORECASE)
REGEX_CHINESE_TEXT = re.compile(r"[a-z0-9'\s\-]+", re.IGNORECASE)
REGEX_INVALID_PATH = re.compile(r'[<>:"|?*]')

try:
    import jieba
    HAS_JIEBA = True
except ImportError:
    HAS_JIEBA = False
# ==============================================


def load_custom_stopwords() -> Set[str]:
    """加载自定义停用词表"""
    stop_words = DEFAULT_STOP_WORDS.copy()
    file_path = input("如需加载自定义停用词表，请输入txt路径（直接回车跳过）：").strip()
    if not file_path:
        return stop_words
    
    if not os.path.isfile(file_path) or not file_path.endswith('.txt'):
        print("[警告] 停用词文件不存在或格式非txt，将使用系统默认停用词。")
        return stop_words
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if word:
                    stop_words.add(word)
        print(f"[*] 成功加载自定义停用词 {len(stop_words) - len(DEFAULT_STOP_WORDS)} 个。")
    except Exception as e:
        print(f"[警告] 读取停用词文件失败：{e}")
    return stop_words


def validate_path(path: str) -> bool:
    """校验路径是否包含非法特殊字符"""
    if REGEX_INVALID_PATH.search(path):
        print(f"[警告] 路径 '{path}' 包含非法特殊字符，操作终止。")
        return False
    return True


def check_dir_writable(dir_path: str) -> bool:
    """提前校验输出目录是否存在写入权限"""
    if not dir_path:
        return True
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path, exist_ok=True)
            return True
        except Exception:
            return False
    return os.access(dir_path, os.W_OK)


def print_progress(current_bytes: int, total_bytes: int):
    """【新增】大文件读取进度提示"""
    if total_bytes > 0:
        percent = (current_bytes / total_bytes) * 100
        print(f"\r[*] 正在读取文件... {percent:.1f}%", end="", flush=True)


def stream_read_text() -> Generator[str, None, None]:
    """
    获取输入文本：支持纯文本、单文件、批量文件夹。
    """
    user_input = input("\n请输入文本、txt文件路径，或包含txt的文件夹路径（如 test.txt 或 ./data）：").strip()
    
    if not user_input:
        yield ""
        return

    # 场景1：输入的是文件夹
    if os.path.isdir(user_input):
        txt_files = glob.glob(os.path.join(user_input, "*.txt"))
        if not txt_files:
            print(f"[警告] 文件夹 '{user_input}' 中没有找到 .txt 文件。")
            yield ""
            return
        print(f"[*] 检测到文件夹，准备批量处理 {len(txt_files)} 个 txt 文件...")
        for file_path in txt_files:
            try:
                if os.path.getsize(file_path) == 0:
                    continue
                for encoding in SUPPORTED_ENCODINGS:
                    try:
                        with open(file_path, 'r', encoding=encoding) as f:
                            for line in f:
                                yield line
                        break
                    except UnicodeDecodeError:
                        continue
            except Exception as e:
                print(f"[警告] 读取文件 {file_path} 失败：{e}")
        return
        
    # 场景2：输入的是文件
    if os.path.isfile(user_input):
        # 【新增】提前校验非法扩展名
        if not user_input.endswith(ALLOWED_EXTENSIONS):
            print(f"[警告] 不支持的文件扩展名，仅支持 {ALLOWED_EXTENSIONS}")
            yield ""
            return
            
        file_size = os.path.getsize(user_input)
        if file_size == 0:
            print("[警告] 输入的文件为空，无法进行统计。")
            yield ""
            return
            
        try:
            for encoding in SUPPORTED_ENCODINGS:
                try:
                    with open(user_input, 'r', encoding=encoding) as f:
                        print(f"[*] 成功打开文件：{user_input}，编码：{encoding}")
                        bytes_read = 0
                        for line in f:
                            bytes_read += len(line.encode(encoding))
                            # 每 1000 行或结尾打印一次进度
                            if bytes_read % 10240 == 0: 
                                print_progress(bytes_read, file_size)
                            yield line
                        print_progress(file_size, file_size) # 打印 100%
                        print() # 换行
                        return
                except UnicodeDecodeError:
                    continue
                    
            print("\n自动识别编码失败，请手动选择编码：")
            print("1. utf-8\n2. gbk\n3. gb2312\n4. latin-1")
            enc_choice = input("请输入对应数字（默认1）：").strip()
            enc_map = {"1": "utf-8", "2": "gbk", "3": "gb2312", "4": "latin-1"}
            selected_enc = enc_map.get(enc_choice, "utf-8")
            try:
                with open(user_input, 'r', encoding=selected_enc) as f:
                    print(f"[*] 使用手动选择的编码 {selected_enc} 打开文件成功")
                    for line in f:
                        yield line
                    return
            except UnicodeDecodeError:
                print("[警告] 手动选择编码仍无法读取文件。")
                yield ""
                return
        except PermissionError:
            print("[警告] 无权限读取该文件。")
            yield ""
        except Exception as e:
            print(f"[警告] 读取文件发生未知错误：{e}")
            yield ""
            
    # 场景3：普通文本
    else:
        if user_input.endswith(ALLOWED_EXTENSIONS) or '/' in user_input or '\\' in user_input:
            if not validate_path(user_input):
                yield ""
                return
            print("[警告] 输入的路径不存在。")
            yield ""
        else:
            print("[提示] 将按普通文本处理。")
            yield user_input


def clean_and_split(line: str, is_case_sensitive: bool = False) -> List[str]:
    """清洗单行文本并分词（支持大小写敏感设置）"""
    if not is_case_sensitive:
        line = line.lower()
    
    if HAS_JIEBA:
        en_num_words = REGEX_EN_NUM.findall(line)
        chinese_text = REGEX_CHINESE_TEXT.sub("", line)
        chinese_words = [w for w in jieba.lcut(chinese_text) if w.strip()]
        return en_num_words + chinese_words
    else:
        return REGEX_WORDS.findall(line)


def count_word_frequency(
    text_stream: Generator[str, None, None], 
    stop_words: Set[str], 
    min_word_len: int = 1,
    is_case_sensitive: bool = False
) -> Dict[str, int]:
    """流式增量统计词频（支持按词长过滤）"""
    counter = Counter()
    for line in text_stream:
        if not line.strip():
            continue
        words = clean_and_split(line, is_case_sensitive)
        # 过滤停用词、无效空字符，并按最小词长过滤
        valid_words = [w for w in words if w not in stop_words and len(w) >= min_word_len]
        counter.update(valid_words)
    return dict(counter)


def export_and_print_result(word_counts: Dict[str, int], threshold: int = 1) -> None:
    """排序、过滤、输出，支持重名文件覆盖提醒"""
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    filtered_words = [item for item in sorted_words if item[1] >= threshold]
    
    if not filtered_words:
        print(f"\n没有出现次数达到 {threshold} 次的词汇。")
        return

    print(f"\n词频统计结果（筛选阈值 ≥ {threshold}）：")
    for word, count in filtered_words[:CONSOLE_OUTPUT_LIMIT]:
        print(f"{word}: {count} 次")
        
    if len(filtered_words) > CONSOLE_OUTPUT_LIMIT:
        print(f"... (共 {len(filtered_words)} 个词汇，完整结果请查看导出文件)")

    fmt = input("\n请选择导出格式（json 或 txt，默认 txt）：").strip().lower()
    if fmt not in ["json", "txt"]:
        fmt = "txt"

    custom_path = input("请输入输出文件路径（直接回车使用默认）：").strip()
    if not custom_path:
        output_path = "word_count_result.json" if fmt == "json" else "word_count_result.txt"
    else:
        if not validate_path(custom_path):
            return
        if fmt == "json" and not custom_path.endswith(".json"):
            output_path = custom_path + ".json"
        elif fmt == "txt" and not custom_path.endswith(".txt"):
            output_path = custom_path + ".txt"
        else:
            output_path = custom_path

    # 【新增】导出时自动检测重名文件并提醒
    if os.path.exists(output_path):
        overwrite = input(f"[提示] 文件 '{output_path}' 已存在，是否覆盖？(y/n，默认y)：").strip().lower()
        if overwrite == 'n':
            print("[提示] 已取消导出。")
            return

    dir_name = os.path.dirname(output_path)
    if dir_name and not check_dir_writable(dir_name):
        print(f"[警告] 目录 '{dir_name}' 无写入权限，导出取消。")
        return

    try:
        if fmt == "json":
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(dict(filtered_words), f, ensure_ascii=False, indent=4)
        else:
            with open(output_path, "w", encoding="utf-8") as f:
                for word, count in filtered_words:
                    f.write(f"{word}: {count}\n")
            
        print(f"[提示] 统计结果已成功导出到 '{output_path}'。")
    except PermissionError:
        print("[警告] 导出失败：当前目录没有写入权限。")
    except OSError as e:
        print(f"[警告] 导出失败：磁盘空间不足或文件被占用。详细信息：{e}")
    except Exception as e:
        print(f"[警告] 导出失败：发生未知异常。详细信息：{e}")


def main() -> None:
    """主控函数"""
    custom_stop_words = load_custom_stopwords()
    
    # 【新增】大小写敏感开关
    case_input = input("是否区分大小写？(y/n，默认不区分)：").strip().lower()
    is_case_sensitive = True if case_input == 'y' else False
    
    # 【新增】最小词长限制
    min_len_input = input("请输入最小词长过滤（直接回车默认1，即不过滤）：").strip()
    min_word_len = int(min_len_input) if min_len_input.isdigit() and int(min_len_input) > 0 else 1

    text_stream = stream_read_text()
    first_line = next(text_stream, "")
    
    if not first_line.strip():
        print("输入为空或读取失败，无法进行词频统计！")
        return
        
    def full_stream():
        yield first_line
        yield from text_stream
        
    word_counts = count_word_frequency(full_stream(), custom_stop_words, min_word_len, is_case_sensitive)
    
    if not word_counts:
        print("未检测到有效词汇，无法统计！")
        return
        
    while True:
        threshold_input = input("请输入词频筛选阈值（直接回车默认1）：").strip()
        if not threshold_input:
            threshold = 1
            break
        try:
            threshold = int(threshold_input)
            if threshold < 1:
                print("[提示] 阈值不能小于 1，请重新输入。")
                continue
            break
        except ValueError:
            print("[错误] 请输入有效的正整数！")

    export_and_print_result(word_counts, threshold)


if __name__ == "__main__":
    main()
"""