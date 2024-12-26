import language_tool_python

def check_grammar(text):
    """Kiểm tra ngữ pháp và chính tả trong văn bản."""
    # Khởi tạo công cụ kiểm tra ngữ pháp với ngôn ngữ tiếng Anh
    tool = language_tool_python.LanguageTool('en-US')

    # Tìm các lỗi ngữ pháp và chính tả trong văn bản
    matches = tool.check(text)

    # Lấy các đề xuất sửa lỗi
    suggestions = []
    for match in matches:
        suggestions.append({
            'context': match.context,
            'suggestions': match.replacements
        })

    return suggestions

def suggest_corrections(text):
    """Trả về các đề xuất sửa lỗi."""
    suggestions = check_grammar(text)
    if not suggestions:
        return "Không tìm thấy lỗi ngữ pháp hoặc chính tả."
    
    correction_details = []
    for suggestion in suggestions:
        context = suggestion['context']
        suggested_corrections = ', '.join(suggestion['suggestions']) if suggestion['suggestions'] else "Không có đề xuất."
        
        correction_details.append(f"Văn bản gốc: {context}\nĐề xuất các từ: {suggested_corrections}\n")

    return "\n".join(correction_details)

# Ví dụ sử dụng
if __name__ == "__main__":
    sample_text = "This is a example of a text with mistakes"
    print(suggest_corrections(sample_text))
