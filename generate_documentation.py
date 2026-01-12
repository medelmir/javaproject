import os
import json
import html

# Base directory
base_dir = r'c:\Users\medel\Desktop\testCapegemini\CapeGeminiBack\polytech'

# File categories
file_structure = {
    'config': [
        'src/main/java/com/polytech/polytech/config/CorsConfig.java',
        'src/main/java/com/polytech/polytech/config/SecurityConfig.java'
    ],
    'controller': [
        'src/main/java/com/polytech/polytech/controller/BoiteController.java',
        'src/main/java/com/polytech/polytech/controller/CoordonneesController.java',
        'src/main/java/com/polytech/polytech/controller/ReservationController.java',
        'src/main/java/com/polytech/polytech/controller/UtilisateurController.java'
    ],
    'dto': [
        'src/main/java/com/polytech/polytech/dto/BoiteRequestDto.java',
        'src/main/java/com/polytech/polytech/dto/BoiteResponseDto.java',
        'src/main/java/com/polytech/polytech/dto/CoordonneesRequestDto.java',
        'src/main/java/com/polytech/polytech/dto/CoordonneesResponseDto.java',
        'src/main/java/com/polytech/polytech/dto/ReservationRequestDto.java',
        'src/main/java/com/polytech/polytech/dto/ReservationResponseDto.java',
        'src/main/java/com/polytech/polytech/dto/UtilisateursRequestDto.java',
        'src/main/java/com/polytech/polytech/dto/UtilisateursResponseDto.java'
    ],
    'entity': [
        'src/main/java/com/polytech/polytech/entity/Boite.java',
        'src/main/java/com/polytech/polytech/entity/Coordonnees.java',
        'src/main/java/com/polytech/polytech/entity/Reservation.java',
        'src/main/java/com/polytech/polytech/entity/ReservationId.java',
        'src/main/java/com/polytech/polytech/entity/Utilisateur.java'
    ],
    'exception': [
        'src/main/java/com/polytech/polytech/exception/BoiteInexistanteException.java',
        'src/main/java/com/polytech/polytech/exception/CoordonneesInexistantesException.java',
        'src/main/java/com/polytech/polytech/exception/GestionnaireException.java',
        'src/main/java/com/polytech/polytech/exception/ReservationInexistanteException.java',
        'src/main/java/com/polytech/polytech/exception/UtilisateurInexistantException.java'
    ],
    'mapper': [
        'src/main/java/com/polytech/polytech/mapper/BoiteMapper.java',
        'src/main/java/com/polytech/polytech/mapper/CoordonneesMapper.java',
        'src/main/java/com/polytech/polytech/mapper/ReservationMapper.java',
        'src/main/java/com/polytech/polytech/mapper/Utilisateursmapper.java'
    ],
    'repository': [
        'src/main/java/com/polytech/polytech/repository/BoiteRepository.java',
        'src/main/java/com/polytech/polytech/repository/CoordonneesRepository.java',
        'src/main/java/com/polytech/polytech/repository/ReservationRepository.java',
        'src/main/java/com/polytech/polytech/repository/Utilisateursrepository.java'
    ],
    'service': [
        'src/main/java/com/polytech/polytech/service/BoiteService.java',
        'src/main/java/com/polytech/polytech/service/CoordonneesService.java',
        'src/main/java/com/polytech/polytech/service/ReservationService.java',
        'src/main/java/com/polytech/polytech/service/UtilisateurService.java'
    ],
    'main': [
        'src/main/java/com/polytech/polytech/PolytechApplication.java'
    ]
}

# Read file content
def read_file(file_path):
    full_path = os.path.join(base_dir, file_path.replace('/', '\\'))
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"// Error reading file: {str(e)}"

# Create file data with content
file_data = {}
for category, files in file_structure.items():
    file_data[category] = []
    for file_path in files:
        file_name = os.path.basename(file_path)
        content = read_file(file_path)
        file_data[category].append({
            'name': file_name,
            'path': file_path,
            'content': html.escape(content)
        })

# Generate JavaScript code with embedded file contents
js_code = "const fileContents = " + json.dumps(file_data, indent=2) + ";"

print("File data generated successfully!")
print(f"Total categories: {len(file_data)}")
for category, files in file_data.items():
    print(f"  {category}: {len(files)} files")

# Save to a JavaScript file
output_file = r'c:\Users\medel\Desktop\testCapegemini\CapeGeminiBack\file-contents.js'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(js_code)

print(f"\nGenerated file: {output_file}")
