from spellchecker import SpellChecker

def check_spelling(text):
    """Kiểm tra chính tả trong văn bản."""
    # Khởi tạo công cụ kiểm tra chính tả
    spell = SpellChecker()

    # Tách văn bản thành các từ
    words = text.split()

    # Tìm các từ sai chính tả
    misspelled = spell.unknown(words)

    # Lấy các đề xuất sửa lỗi
    suggestions = []
    for word in misspelled:
        suggestions.append({
            'word': word,
            'suggestions': spell.candidates(word)
        })

    return suggestions

def suggest_corrections(text):
    """Trả về các đề xuất sửa lỗi chính tả."""
    suggestions = check_spelling(text)
    if not suggestions:
        return "Không tìm thấy lỗi chính tả."

    correction_details = []
    for suggestion in suggestions:
        word = suggestion['word']
        suggested_corrections = ', '.join(suggestion['suggestions']) if suggestion['suggestions'] else "Không có đề xuất."
        
        correction_details.append(f"Từ sai: {word}\nĐề xuất các từ: {suggested_corrections}\n")

    return "\n".join(correction_details)

# Ví dụ sử dụng
if __name__ == "__main__":
    sample_text = "This is a exemple of a text with mistaks"
    print(suggest_corrections(sample_text))
