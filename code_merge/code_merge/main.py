import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import argparse

entry_dir = None
entry_output = None

file_extensions = (
    # 常见编程语言
    '.py', '.java', '.cpp', '.c', '.cs', '.go', '.rs', '.swift', '.kt', '.scala',
    '.js', '.ts', '.jsx', '.tsx', '.php', '.rb', '.pl', '.sh', '.bash', '.ps1',
    # Web 开发
    '.html', '.htm', '.css', '.scss', '.sass', '.less',
    # 标记语言
    '.md', '.markdown', '.rst', '.tex', '.textile',
    # 数据交换和配置文件
    '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf',
    # 数据库和查询语言
    '.sql', '.graphql',
    # 模板语言
    '.jinja', '.jinja2', '.twig', '.mustache', '.handlebars',
    # 移动开发
    '.swift', '.kt', '.kts', '.dart',
    # 其他脚本语言
    '.lua', '.groovy', '.r', '.matlab',
    # 函数式编程语言
    '.hs', '.ml', '.clj', '.elm',
    # 系统和低级编程
    '.asm', '.s',
    # 特定领域语言
    '.dockerfile', '.makefile', '.cmake',
    # 版本控制和项目配置
    '.gitignore', '.gitattributes', '.editorconfig',
    # 文档和纯文本
    '.txt', '.log', '.csv',
    # XML 相关
    '.xml', '.xsl', '.xslt', '.svg', '.plist',
    # 其他常见格式
    '.properties', '.env'
)

def code_merge(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'rb') as infile:
                            content = infile.read()
                        
                        # 尝试用 UTF-8 解码，对于无法解码的字符替换为空格
                        decoded_content = content.decode('utf-8', errors='replace')
                        
                        # 将 Unicode 替换字符 (�) 替换为空格
                        decoded_content = decoded_content.replace('\ufffd', ' ')
                        
                        outfile.write(f"========={file_path}========\n")
                        outfile.write(decoded_content)
                        outfile.write(f"\n========={file_path}========\n\n")
                    except Exception as e:
                        print(f"Error processing file {file_path}: {str(e)}")

def select_directory():
    global entry_dir, entry_output
    directory = filedialog.askdirectory()
    entry_dir.delete(0, tk.END)
    entry_dir.insert(0, directory)
    
    # 获取目录的最后一个部分作为默认文件名
    default_filename = os.path.basename(directory) + ".txt"
    entry_output.delete(0, tk.END)
    entry_output.insert(0, default_filename)

def submit():
    global entry_dir, entry_output
    directory = entry_dir.get()
    base_path = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(base_path, entry_output.get())
    if not directory or not output_file:
        messagebox.showwarning("Input Error", "Please enter both directory and output file name.")
        return
    
    # 确保输出文件有 .txt 扩展名
    if not output_file.lower().endswith('.txt'):
        output_file += '.txt'
    
    code_merge(directory, output_file)
    messagebox.showinfo("Success", f"Code files have been consolidated into {output_file}.")

def run_gui():
    global entry_dir, entry_output
    app = tk.Tk()
    app.title("Code Consolidator")

    frame = tk.Frame(app)
    frame.pack(padx=10, pady=10)

    label_dir = tk.Label(frame, text="Select Project Directory:")
    label_dir.grid(row=0, column=0, sticky="w")

    entry_dir = tk.Entry(frame, width=50)
    entry_dir.grid(row=0, column=1, padx=5)

    button_browse = tk.Button(frame, text="Browse...", command=select_directory)
    button_browse.grid(row=0, column=2)

    label_output = tk.Label(frame, text="Output File Name:")
    label_output.grid(row=1, column=0, sticky="w")

    entry_output = tk.Entry(frame, width=50)
    entry_output.grid(row=1, column=1, padx=5)

    button_submit = tk.Button(frame, text="Submit", command=submit)
    button_submit.grid(row=2, column=1, pady=10)

    app.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Consolidate code files from a directory.")
    parser.add_argument("-p", "--path", help="Path to the project directory")
    parser.add_argument("-o", "--output", help="Output file name", default="consolidated_code.txt")
    args = parser.parse_args()

    if args.path:
        base_path = os.path.dirname(os.path.abspath(__file__))
        output_file = os.path.join(base_path, args.output)
        code_merge(args.path, output_file)
        print(f"Code files have been consolidated into {output_file}.")
    else:
        run_gui()

if __name__ == "__main__":
    main()
