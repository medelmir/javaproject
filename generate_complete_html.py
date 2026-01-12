import os
import html as html_module

# Base directory
base_dir = r'c:\Users\medel\Desktop\testCapegemini\CapeGeminiBack\polytech'

# File categories with their metadata
categories = {
    'main': {
        'title': 'Application Entry Point',
        'icon': '🚀',
        'files': ['src/main/java/com/polytech/polytech/PolytechApplication.java']
    },
    'config': {
        'title': 'Configuration Files',
        'icon': '⚙️',
        'files': [
            'src/main/java/com/polytech/polytech/config/CorsConfig.java',
            'src/main/java/com/polytech/polytech/config/SecurityConfig.java'
        ]
    },
    'controller': {
        'title': 'REST Controllers',
        'icon': '🎮',
        'files': [
            'src/main/java/com/polytech/polytech/controller/BoiteController.java',
            'src/main/java/com/polytech/polytech/controller/CoordonneesController.java',
            'src/main/java/com/polytech/polytech/controller/ReservationController.java',
            'src/main/java/com/polytech/polytech/controller/UtilisateurController.java'
        ]
    },
    'service': {
        'title': 'Business Services',
        'icon': '⚡',
        'files': [
            'src/main/java/com/polytech/polytech/service/BoiteService.java',
            'src/main/java/com/polytech/polytech/service/CoordonneesService.java',
            'src/main/java/com/polytech/polytech/service/ReservationService.java',
            'src/main/java/com/polytech/polytech/service/UtilisateurService.java'
        ]
    },
    'entity': {
        'title': 'JPA Entities',
        'icon': '🗃️',
        'files': [
            'src/main/java/com/polytech/polytech/entity/Boite.java',
            'src/main/java/com/polytech/polytech/entity/Coordonnees.java',
            'src/main/java/com/polytech/polytech/entity/Reservation.java',
            'src/main/java/com/polytech/polytech/entity/ReservationId.java',
            'src/main/java/com/polytech/polytech/entity/Utilisateur.java'
        ]
    },
    'dto': {
        'title': 'Data Transfer Objects',
        'icon': '📦',
        'files': [
            'src/main/java/com/polytech/polytech/dto/BoiteRequestDto.java',
            'src/main/java/com/polytech/polytech/dto/BoiteResponseDto.java',
            'src/main/java/com/polytech/polytech/dto/CoordonneesRequestDto.java',
            'src/main/java/com/polytech/polytech/dto/CoordonneesResponseDto.java',
            'src/main/java/com/polytech/polytech/dto/ReservationRequestDto.java',
            'src/main/java/com/polytech/polytech/dto/ReservationResponseDto.java',
            'src/main/java/com/polytech/polytech/dto/UtilisateursRequestDto.java',
            'src/main/java/com/polytech/polytech/dto/UtilisateursResponseDto.java'
        ]
    },
    'repository': {
        'title': 'Data Repositories',
        'icon': '💾',
        'files': [
            'src/main/java/com/polytech/polytech/repository/BoiteRepository.java',
            'src/main/java/com/polytech/polytech/repository/CoordonneesRepository.java',
            'src/main/java/com/polytech/polytech/repository/ReservationRepository.java',
            'src/main/java/com/polytech/polytech/repository/Utilisateursrepository.java'
        ]
    },
    'mapper': {
        'title': 'Entity-DTO Mappers',
        'icon': '🔄',
        'files': [
            'src/main/java/com/polytech/polytech/mapper/BoiteMapper.java',
            'src/main/java/com/polytech/polytech/mapper/CoordonneesMapper.java',
            'src/main/java/com/polytech/polytech/mapper/ReservationMapper.java',
            'src/main/java/com/polytech/polytech/mapper/Utilisateursmapper.java'
        ]
    },
    'exception': {
        'title': 'Exception Handlers',
        'icon': '⚠️',
        'files': [
            'src/main/java/com/polytech/polytech/exception/BoiteInexistanteException.java',
            'src/main/java/com/polytech/polytech/exception/CoordonneesInexistantesException.java',
            'src/main/java/com/polytech/polytech/exception/GestionnaireException.java',
            'src/main/java/com/polytech/polytech/exception/ReservationInexistanteException.java',
            'src/main/java/com/polytech/polytech/exception/UtilisateurInexistantException.java'
        ]
    }
}

def read_file(file_path):
    """Read file content"""
    full_path = os.path.join(base_dir, file_path.replace('/', '\\'))
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"// Error reading file: {str(e)}"

def generate_file_card(file_path, file_index, category_key):
    """Generate HTML for a single file card"""
    file_name = os.path.basename(file_path)
    content = read_file(file_path)
    escaped_content = html_module.escape(content)
    
    code_id = f"{category_key}-{file_index}"
    
    return f'''
            <div class="file-card">
                <div class="file-header">
                    <div class="file-info">
                        <div class="file-name">{file_name}</div>
                        <div class="file-path">{file_path}</div>
                    </div>
                    <button class="copy-btn" onclick="copyCode('{code_id}')">📋 Copy</button>
                </div>
                <pre><code class="language-java" id="code-{code_id}">{escaped_content}</code></pre>
            </div>
'''

def generate_category_section(category_key, category_data):
    """Generate HTML for a category section"""
    files_html = ""
    for idx, file_path in enumerate(category_data['files'], 1):
        files_html += generate_file_card(file_path, idx, category_key)
    
    return f'''
        <!-- {category_data['title'].upper()} -->
        <div class="category-section">
            <div class="category-header">
                <div class="category-icon">{category_data['icon']}</div>
                <h2>{category_data['title']}</h2>
                <div class="file-count">{len(category_data['files'])} files</div>
            </div>
{files_html}
        </div>
'''

# Generate all category sections
all_sections = ""
total_files = 0
for category_key, category_data in categories.items():
    all_sections += generate_category_section(category_key, category_data)
    total_files += len(category_data['files'])

# HTML Template
html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Polytech Project - Complete Code Repository</title>
    <meta name="description" content="Complete code repository for the Polytech Capgemini project with all source files visible.">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    
    <!-- Highlight.js for Syntax Highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/java.min.js"></script>
    
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --accent-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            --success-gradient: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            --dark-bg: #0f0f23;
            --darker-bg: #0a0a15;
            --card-bg: rgba(255, 255, 255, 0.03);
            --card-border: rgba(255, 255, 255, 0.1);
            --text-primary: #e0e0e0;
            --text-secondary: #a0a0a0;
            --text-accent: #667eea;
            --code-bg: #282c34;
        }}

        body {{
            font-family: 'Inter', sans-serif;
            background: var(--dark-bg);
            color: var(--text-primary);
            line-height: 1.6;
            overflow-x: hidden;
        }}

        /* Animated Background */
        .background-animation {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            overflow: hidden;
        }}

        .background-animation::before {{
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle at 20% 50%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 80% 80%, rgba(118, 75, 162, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 40% 20%, rgba(79, 172, 254, 0.1) 0%, transparent 50%);
            animation: backgroundMove 20s ease-in-out infinite;
        }}

        @keyframes backgroundMove {{
            0%, 100% {{ transform: translate(0, 0); }}
            50% {{ transform: translate(-50px, -50px); }}
        }}

        /* Header */
        header {{
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--card-border);
            padding: 2rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        }}

        .header-content {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
        }}

        h1 {{
            font-size: 2.5rem;
            font-weight: 700;
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }}

        .subtitle {{
            color: var(--text-secondary);
            font-size: 1.1rem;
        }}

        /* Main Content */
        main {{
            max-width: 1400px;
            margin: 2rem auto;
            padding: 0 2rem 4rem;
        }}

        /* Stats Section */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }}

        .stat-card {{
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 1.5rem;
            transition: all 0.3s ease;
        }}

        .stat-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(102, 126, 234, 0.2);
            border-color: var(--text-accent);
        }}

        .stat-number {{
            font-size: 2.5rem;
            font-weight: 700;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .stat-label {{
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }}

        /* Category Section */
        .category-section {{
            margin-bottom: 4rem;
        }}

        .category-header {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--card-border);
            border-radius: 16px;
        }}

        .category-icon {{
            width: 50px;
            height: 50px;
            border-radius: 12px;
            background: var(--primary-gradient);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }}

        .category-header h2 {{
            font-size: 1.8rem;
            font-weight: 600;
            color: var(--text-primary);
        }}

        .file-count {{
            margin-left: auto;
            padding: 0.5rem 1rem;
            background: var(--success-gradient);
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
        }}

        /* File Card */
        .file-card {{
            background: var(--card-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            overflow: hidden;
            margin-bottom: 2rem;
            transition: all 0.3s ease;
        }}

        .file-card:hover {{
            border-color: var(--text-accent);
            box-shadow: 0 8px 30px rgba(102, 126, 234, 0.2);
        }}

        .file-header {{
            padding: 1.5rem;
            background: rgba(0, 0, 0, 0.2);
            border-bottom: 1px solid var(--card-border);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .file-info {{
            flex: 1;
        }}

        .file-name {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text-accent);
            margin-bottom: 0.25rem;
        }}

        .file-path {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            color: var(--text-secondary);
        }}

        .copy-btn {{
            padding: 0.6rem 1.2rem;
            background: var(--primary-gradient);
            border: none;
            border-radius: 8px;
            color: white;
            cursor: pointer;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }}

        .copy-btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }}

        .copy-btn:active {{
            transform: scale(0.95);
        }}

        pre {{
            margin: 0;
            padding: 0;
            background: var(--code-bg);
            overflow-x: auto;
        }}

        pre code {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            line-height: 1.6;
            display: block;
            padding: 1.5rem;
        }}

        /* Toast Notification */
        .toast {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            padding: 1rem 1.5rem;
            background: var(--success-gradient);
            color: white;
            border-radius: 12px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
            transform: translateY(200%);
            transition: transform 0.3s ease;
            z-index: 1000;
            font-weight: 500;
        }}

        .toast.show {{
            transform: translateY(0);
        }}

        /* Scrollbar */
        ::-webkit-scrollbar {{
            width: 12px;
            height: 12px;
        }}

        ::-webkit-scrollbar-track {{
            background: var(--darker-bg);
        }}

        ::-webkit-scrollbar-thumb {{
            background: var(--primary-gradient);
            border-radius: 6px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: var(--secondary-gradient);
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            h1 {{
                font-size: 2rem;
            }}

            .file-header {{
                flex-direction: column;
                align-items: flex-start;
                gap: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="background-animation"></div>

    <header>
        <div class="header-content">
            <h1>🎓 Polytech Project - Complete Code Repository</h1>
            <p class="subtitle">Capgemini Backend | Spring Boot Application | All {total_files} Source Files Visible</p>
        </div>
    </header>

    <main>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{total_files}</div>
                <div class="stat-label">Total Java Files</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">4</div>
                <div class="stat-label">REST Controllers</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">4</div>
                <div class="stat-label">Business Services</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">5</div>
                <div class="stat-label">JPA Entities</div>
            </div>
        </div>

{all_sections}
    </main>

    <div class="toast" id="toast">✓ Code copied to clipboard!</div>

    <script>
        // Copy code to clipboard
        function copyCode(id) {{
            const codeElement = document.getElementById('code-' + id);
            const content = codeElement.textContent;
            
            navigator.clipboard.writeText(content).then(() => {{
                showToast();
            }}).catch(err => {{
                console.error('Failed to copy:', err);
            }});
        }}

        // Show toast notification
        function showToast() {{
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => {{
                toast.classList.remove('show');
            }}, 2000);
        }}

        // Initialize syntax highlighting
        window.onload = function() {{
            hljs.highlightAll();
            console.log('Loaded {total_files} Java files successfully!');
        }};
    </script>
</body>
</html>'''

# Write the HTML file
output_file = r'c:\Users\medel\Desktop\testCapegemini\CapeGeminiBack\polytech-all-code-visible.html'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"[SUCCESS] Generated HTML file with {total_files} Java files!")
print(f"Output file: {output_file}")
print(f"\nFile breakdown:")
for category_key, category_data in categories.items():
    print(f"  {category_data['title']}: {len(category_data['files'])} files")
