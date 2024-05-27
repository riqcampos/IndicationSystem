import numpy as np
import pandas as pd
from scipy.stats import pearsonr as cor

class PersonR():
    Fields = ["Estabelecer um ambiente de concentracao",
              "Aprofundamento por material teorico",
              "Estudo por meio de aulas complementares",
              "Estudo por discencia",
              "Curiosidade individual",
              "Estabelecimento de rotina",
              "Longos Periodos de Estudo",
              "Resolucao de problemas externos",
              "Tempo de antecedenta para assimilacao"]
    
    def __init__(self, entry: dict):
        self.entry = entry
        self.corMatriz = np.zeros((len(entry), len(entry)))
        self.fillCorMatrix()

    def calculate_correlation(self, user1, user2):
        correlation, _ = cor(user1, user2)
        return correlation

    def fillCorMatrix(self):
        for i, (user1, data1) in enumerate(self.entry.items()):
            for j, (user2, data2) in enumerate(self.entry.items()):
                correlation = self.calculate_correlation(data1, data2)
                self.corMatriz[i][j] = correlation

    def recommend_fields_for_user(self, user):
        user_data = self.entry[user]
        user_correlation = self.corMatriz[list(self.entry.keys()).index(user)]
        field_scores = {}
        for i, field in enumerate(self.Fields):
            field_data = [data[i] for data in self.entry.values()]
            field_scores[field] = np.dot(user_data[:len(field_data)], field_data) / (np.linalg.norm(user_data) * np.linalg.norm(field_data))
        recommended_fields = [field for field, score in sorted(field_scores.items(), key=lambda x: x[1], reverse=True)[:3]]
        return recommended_fields
    
    def finish(self):
        user_recommendations = {}
        for user in self.entry.keys():
            recommended_fields = self.recommend_fields_for_user(user)
            user_recommendations[user] = recommended_fields
            print(f"Usuário {user} deve considerar os seguintes campos:")
            for field in recommended_fields:
                print(f"- {field}")
            print()
        
        # Criar um DataFrame com as recomendações
        df_recommendations = pd.DataFrame(user_recommendations)
        
        # Salvar o DataFrame em um arquivo CSV
        df_recommendations.to_csv('recomendacoes_campos_por_usuario.csv', index=False)

# Dados dos usuários (exemplo)
Entry = {
    "Usuario1": [5, 4, 3, 2, 4, 5, 3, 2, 4],
    "Usuario2": [3, 2, 4, 5, 3, 3, 4, 5, 2],
    "Usuario3": [4, 5, 2, 3, 5, 4, 2, 3, 5],
    "Usuario4": [2, 3, 5, 4, 2, 2, 5, 4, 3],
    "Usuario5": [5, 4, 3, 2, 4, 5, 3, 2, 4]
}

# Instanciar a classe e executar o sistema de recomendação
person_r = PersonR(Entry)
person_r.finish()