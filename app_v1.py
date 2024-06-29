from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/skincare-routines', methods=['GET'])
def get_skincare_routines():
    skincare_routines = [
        {
            "routine_name": "Anti-Aging Routine",
            "steps": [
                {"step": "Cleanser", "description": "Use a gentle cleanser to remove impurities."},
                {"step": "Toner", "description": "Apply a hydrating toner to balance the skin."},
                {"step": "Serum", "description": "Use a serum with antioxidants and peptides."},
                {"step": "Moisturizer", "description": "Apply a rich moisturizer to hydrate the skin."},
                {"step": "Sunscreen", "description": "Use a broad-spectrum sunscreen with SPF 30 or higher."}
            ]
        },
        {
            "routine_name": "Acne-Prone Skin Routine",
            "steps": [
                {"step": "Cleanser", "description": "Use a cleanser with salicylic acid to fight acne."},
                {"step": "Toner", "description": "Apply a toner with witch hazel to reduce oil."},
                {"step": "Serum", "description": "Use a serum with niacinamide to reduce inflammation."},
                {"step": "Moisturizer", "description": "Apply a lightweight, non-comedogenic moisturizer."},
                {"step": "Sunscreen", "description": "Use an oil-free sunscreen with SPF 30 or higher."}
            ]
        }
    ]
    return jsonify(skincare_routines)

if __name__ == '__main__':
    app.run(debug=True)

