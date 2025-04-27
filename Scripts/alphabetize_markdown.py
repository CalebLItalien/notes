import re

def sort_bullets_in_section(section):
    """Sort bullet points in a section while preserving the section header."""
    lines = section.split('\n')
    header = lines[0]
    bullets = [line.strip() for line in lines[1:] if line.strip()]
    
    sorted_bullets = sorted(bullets, key=lambda x: re.sub(r'^-\s*', '', x).lower())
    
    return '\n'.join([header] + sorted_bullets)

def process_markdown(content):
    """Process the markdown content section by section."""
    sections = re.split(r'(?m)^(#+\s+.+)$', content)
    
    processed_sections = []
    current_section = ""
    
    for i, section in enumerate(sections):
        if not section.strip():
            continue
            
        if re.match(r'^#+\s+.+$', section):
            if current_section:
                processed_sections.append(sort_bullets_in_section(current_section))
                current_section = ""
            current_section = section
        else:
            if current_section:
                current_section += '\n' + section
            else:
                current_section = section
                
    if current_section:
        processed_sections.append(sort_bullets_in_section(current_section))
    
    return '\n'.join(processed_sections)

def main():
    file_path = 'your_file.md'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    processed_content = process_markdown(content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(processed_content)
    
    print(f"Markdown file {file_path} has been updated with sorted bullet points")

if __name__ == "__main__":
    main()