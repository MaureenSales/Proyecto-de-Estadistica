# kaggle_downloader.py

import os
from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleViolenceDownloader:
    """Descargador automatizado de datasets de Kaggle"""
    
    def __init__(self, output_dir='data/raw/kaggle'):
        self.api = KaggleApi()
        self.api.authenticate()
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def download_dataset(self, dataset_slug, unzip=True):
        """Descarga un dataset específico"""
        print(f"📥 Descargando: {dataset_slug}")
        
        try:
            self.api.dataset_download_files(
                dataset_slug,
                path=self.output_dir,
                unzip=unzip
            )
            print(f"✅ Descargado: {dataset_slug}")
            return True
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False
    
    def download_all_violence_datasets(self):
        """Descarga todos los datasets recomendados"""
        
        datasets = {
            'violence_women_girls': 'andrewmvd/violence-against-women-and-girls',
            'us_homicides': 'murderaccountability/homicide-reports',
            'uk_domestic_violence': 'mpwolke/cusersmarildownloadsdomviolcsv',
            'rural_domestic_violence': 'fahmidachowdhury/domestic-violence-against-women',
            'global_homicides': 'programmerrdai/homicides',
        }
        
        results = {}
        
        for name, slug in datasets.items():
            print(f"\n{'='*60}")
            results[name] = self.download_dataset(slug)
        
        print(f"\n{'='*60}")
        print(f"✅ Completados: {sum(results.values())}/{len(results)}")
        
        return results

# Uso
if __name__ == '__main__':
    downloader = KaggleViolenceDownloader()
    downloader.download_all_violence_datasets()