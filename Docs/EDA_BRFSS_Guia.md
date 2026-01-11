# Análisis Exploratorio de Datos (EDA) - BRFSS
## Guía Completa con Código Python

---

## Estructura del EDA según el Proyecto

El epígrafe 3.2 requiere:
1. ✅ Estadísticos descriptivos (tendencia central y dispersión)
2. ✅ Visualizaciones clave (histogramas, boxplots, dispersión, correlaciones)
3. ✅ Discusión de hallazgos relacionados con preguntas de investigación

---

# PASO 0: Configuración Inicial

```python
# Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configuración de visualización
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
sns.set_palette("husl")

# Cargar datos (ejemplo con archivo XPT de BRFSS)
# Opción 1: Desde archivo SAS XPT
# df = pd.read_sas('LLCP2022.XPT', format='xport')

# Opción 2: Desde CSV procesado
# df = pd.read_csv('brfss_2022.csv')

# Para este ejemplo, asumimos que ya tienes el DataFrame cargado
print(f"Dimensiones del dataset: {df.shape}")
print(f"Filas: {df.shape[0]:,}")
print(f"Columnas: {df.shape[1]}")
```

---

# PASO 1: Exploración Inicial del Dataset

## 1.1 Vista General de los Datos

```python
def exploracion_inicial(df):
    """
    Función para exploración inicial del dataset
    """
    print("="*60)
    print("EXPLORACIÓN INICIAL DEL DATASET")
    print("="*60)
    
    # Dimensiones
    print(f"\n📊 Dimensiones: {df.shape[0]:,} filas × {df.shape[1]} columnas")
    
    # Primeras filas
    print("\n📋 Primeras 5 filas:")
    display(df.head())
    
    # Tipos de datos
    print("\n🔤 Tipos de datos:")
    print(df.dtypes.value_counts())
    
    # Memoria utilizada
    memoria = df.memory_usage(deep=True).sum() / 1024**2
    print(f"\n💾 Memoria utilizada: {memoria:.2f} MB")
    
    return None

exploracion_inicial(df)
```

## 1.2 Selección de Variables Relevantes

```python
# Definir variables de interés para el análisis
# (Ajustar según tus preguntas de investigación)

variables_analisis = {
    # Variables de salud
    'GENHLTH': 'Salud general (1-5)',
    'PHYSHLTH': 'Días mala salud física (0-30)',
    'MENTHLTH': 'Días mala salud mental (0-30)',
    'POORHLTH': 'Días con limitaciones (0-30)',
    
    # Variables demográficas
    '_AGE80': 'Edad (18-80)',
    'SEX': 'Sexo (1=M, 2=F)',
    '_EDUCAG': 'Nivel educativo (1-4)',
    '_INCOMG': 'Nivel de ingreso (1-5)',
    
    # Variables de comportamiento
    '_RFSMOK3': 'Fumador actual (1=No, 2=Sí)',
    '_RFBING5': 'Bebedor excesivo (1=No, 2=Sí)',
    '_BMI5': 'IMC (×100)',
    '_TOTINDA': 'Actividad física (1=Activo, 2=Inactivo)',
    'SLEPTIM1': 'Horas de sueño',
    
    # Variables de condiciones crónicas
    'DIABETE3': 'Diabetes (1=Sí, 2=No, 3=Pre/Embarazo)',
    'ADDEPEV2': 'Depresión diagnosticada (1=Sí, 2=No)',
    '_RFHYPE5': 'Hipertensión (1=No, 2=Sí)',
}

# Seleccionar solo variables disponibles en el dataset
vars_disponibles = [v for v in variables_analisis.keys() if v in df.columns]
df_analisis = df[vars_disponibles].copy()

print(f"Variables seleccionadas para análisis: {len(vars_disponibles)}")
for var in vars_disponibles:
    print(f"  • {var}: {variables_analisis[var]}")
```

---

# PASO 2: Análisis de Valores Faltantes

```python
def analisis_missing(df):
    """
    Análisis detallado de valores faltantes
    """
    print("="*60)
    print("ANÁLISIS DE VALORES FALTANTES")
    print("="*60)
    
    # Calcular missings por columna
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    
    # Crear DataFrame resumen
    missing_df = pd.DataFrame({
        'Variable': missing.index,
        'Faltantes': missing.values,
        'Porcentaje': missing_pct.values
    }).sort_values('Porcentaje', ascending=False)
    
    missing_df = missing_df[missing_df['Faltantes'] > 0]
    
    if len(missing_df) == 0:
        print("\n✅ No hay valores faltantes en el dataset")
    else:
        print(f"\n⚠️ Variables con valores faltantes: {len(missing_df)}")
        print(missing_df.to_string(index=False))
    
    # Visualización
    if len(missing_df) > 0:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Gráfico de barras
        top_missing = missing_df.head(15)
        axes[0].barh(top_missing['Variable'], top_missing['Porcentaje'], color='coral')
        axes[0].set_xlabel('Porcentaje de valores faltantes')
        axes[0].set_title('Top 15 Variables con Valores Faltantes')
        axes[0].invert_yaxis()
        
        # Mapa de calor de missings (muestra de filas)
        sample_size = min(1000, len(df))
        sample_df = df.sample(n=sample_size, random_state=42)
        
        sns.heatmap(sample_df[missing_df['Variable'].head(15)].isnull(), 
                    cbar=True, yticklabels=False, ax=axes[1], cmap='YlOrRd')
        axes[1].set_title(f'Patrón de Valores Faltantes (muestra n={sample_size})')
        
        plt.tight_layout()
        plt.savefig('eda_missing_values.png', dpi=150, bbox_inches='tight')
        plt.show()
    
    return missing_df

missing_df = analisis_missing(df_analisis)
```

---

# PASO 3: Estadísticos Descriptivos

## 3.1 Variables Numéricas

```python
def estadisticos_numericos(df):
    """
    Estadísticos descriptivos para variables numéricas
    """
    print("="*60)
    print("ESTADÍSTICOS DESCRIPTIVOS - VARIABLES NUMÉRICAS")
    print("="*60)
    
    # Identificar variables numéricas
    vars_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
    
    # Calcular estadísticos
    stats_df = pd.DataFrame()
    
    for var in vars_numericas:
        col = df[var].dropna()
        
        stats_var = {
            'Variable': var,
            'N': len(col),
            'Media': col.mean(),
            'Mediana': col.median(),
            'Moda': col.mode().iloc[0] if len(col.mode()) > 0 else np.nan,
            'Desv. Std': col.std(),
            'Varianza': col.var(),
            'Mín': col.min(),
            'Q1 (25%)': col.quantile(0.25),
            'Q3 (75%)': col.quantile(0.75),
            'Máx': col.max(),
            'Rango': col.max() - col.min(),
            'IQR': col.quantile(0.75) - col.quantile(0.25),
            'Asimetría': col.skew(),
            'Curtosis': col.kurtosis()
        }
        stats_df = pd.concat([stats_df, pd.DataFrame([stats_var])], ignore_index=True)
    
    # Formatear para mejor visualización
    stats_df = stats_df.round(3)
    
    print("\n📊 Medidas de Tendencia Central y Dispersión:\n")
    print(stats_df.to_string(index=False))
    
    # Guardar como CSV
    stats_df.to_csv('estadisticos_descriptivos.csv', index=False)
    print("\n💾 Guardado en 'estadisticos_descriptivos.csv'")
    
    return stats_df

stats_numericos = estadisticos_numericos(df_analisis)
```

## 3.2 Variables Categóricas

```python
def estadisticos_categoricos(df, variables_cat=None):
    """
    Estadísticos descriptivos para variables categóricas
    """
    print("="*60)
    print("ESTADÍSTICOS DESCRIPTIVOS - VARIABLES CATEGÓRICAS")
    print("="*60)
    
    # Variables categóricas en BRFSS (aunque sean numéricas, son categorías)
    if variables_cat is None:
        variables_cat = ['GENHLTH', 'SEX', '_EDUCAG', '_INCOMG', '_RFSMOK3', 
                         '_RFBING5', '_TOTINDA', 'DIABETE3', 'ADDEPEV2']
    
    variables_cat = [v for v in variables_cat if v in df.columns]
    
    for var in variables_cat:
        print(f"\n{'─'*40}")
        print(f"📌 {var}")
        print(f"{'─'*40}")
        
        # Frecuencias
        freq = df[var].value_counts(dropna=False)
        pct = df[var].value_counts(normalize=True, dropna=False) * 100
        
        resumen = pd.DataFrame({
            'Valor': freq.index,
            'Frecuencia': freq.values,
            'Porcentaje': pct.values.round(2)
        })
        
        print(resumen.to_string(index=False))
        
        # Moda
        moda = df[var].mode()
        if len(moda) > 0:
            print(f"\n  Moda: {moda.iloc[0]} ({pct.iloc[0]:.1f}%)")

estadisticos_categoricos(df_analisis)
```

## 3.3 Resumen Ejecutivo de Estadísticos

```python
def resumen_ejecutivo(df):
    """
    Genera un resumen ejecutivo del dataset
    """
    print("="*60)
    print("RESUMEN EJECUTIVO DEL DATASET")
    print("="*60)
    
    n = len(df)
    
    # Calcular estadísticos clave
    resumen = {}
    
    # Salud general
    if 'GENHLTH' in df.columns:
        buena_salud = (df['GENHLTH'].isin([1, 2, 3])).sum() / df['GENHLTH'].notna().sum() * 100
        resumen['Buena salud autopercibida'] = f"{buena_salud:.1f}%"
    
    # Salud mental
    if 'MENTHLTH' in df.columns:
        media_mental = df['MENTHLTH'].mean()
        resumen['Días promedio mala salud mental'] = f"{media_mental:.1f}"
    
    # Salud física
    if 'PHYSHLTH' in df.columns:
        media_fisica = df['PHYSHLTH'].mean()
        resumen['Días promedio mala salud física'] = f"{media_fisica:.1f}"
    
    # Demografía
    if 'SEX' in df.columns:
        pct_mujeres = (df['SEX'] == 2).sum() / df['SEX'].notna().sum() * 100
        resumen['Porcentaje mujeres'] = f"{pct_mujeres:.1f}%"
    
    if '_AGE80' in df.columns:
        edad_media = df['_AGE80'].mean()
        resumen['Edad promedio'] = f"{edad_media:.1f} años"
    
    # Comportamientos de riesgo
    if '_RFSMOK3' in df.columns:
        fumadores = (df['_RFSMOK3'] == 2).sum() / df['_RFSMOK3'].notna().sum() * 100
        resumen['Fumadores actuales'] = f"{fumadores:.1f}%"
    
    if '_RFBMI5' in df.columns:
        sobrepeso = (df['_RFBMI5'] == 2).sum() / df['_RFBMI5'].notna().sum() * 100
        resumen['Sobrepeso/Obesidad'] = f"{sobrepeso:.1f}%"
    
    if 'SLEPTIM1' in df.columns:
        sueno_medio = df['SLEPTIM1'].mean()
        poco_sueno = (df['SLEPTIM1'] < 7).sum() / df['SLEPTIM1'].notna().sum() * 100
        resumen['Horas de sueño promedio'] = f"{sueno_medio:.1f}"
        resumen['Duermen menos de 7 horas'] = f"{poco_sueno:.1f}%"
    
    # Condiciones crónicas
    if 'ADDEPEV2' in df.columns:
        depresion = (df['ADDEPEV2'] == 1).sum() / df['ADDEPEV2'].notna().sum() * 100
        resumen['Depresión diagnosticada'] = f"{depresion:.1f}%"
    
    print(f"\n📈 Muestra total: {n:,} individuos\n")
    
    for key, value in resumen.items():
        print(f"  • {key}: {value}")
    
    return resumen

resumen = resumen_ejecutivo(df_analisis)
```

---

# PASO 4: Visualizaciones

## 4.1 Histogramas - Distribución de Variables Numéricas

```python
def plot_histogramas(df, variables=None, bins=30):
    """
    Histogramas para variables numéricas
    """
    if variables is None:
        variables = ['MENTHLTH', 'PHYSHLTH', '_AGE80', 'SLEPTIM1', '_BMI5']
    
    variables = [v for v in variables if v in df.columns]
    n_vars = len(variables)
    
    if n_vars == 0:
        print("No hay variables para graficar")
        return
    
    # Calcular filas y columnas
    n_cols = min(3, n_vars)
    n_rows = (n_vars + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows))
    if n_vars == 1:
        axes = [axes]
    else:
        axes = axes.flatten()
    
    for i, var in enumerate(variables):
        ax = axes[i]
        data = df[var].dropna()
        
        # Histograma con KDE
        ax.hist(data, bins=bins, density=True, alpha=0.7, color='steelblue', 
                edgecolor='white')
        
        # Línea de densidad KDE
        if len(data) > 10:
            data.plot.kde(ax=ax, color='darkred', linewidth=2)
        
        # Líneas de media y mediana
        media = data.mean()
        mediana = data.median()
        ax.axvline(media, color='red', linestyle='--', linewidth=1.5, 
                   label=f'Media: {media:.1f}')
        ax.axvline(mediana, color='green', linestyle=':', linewidth=1.5, 
                   label=f'Mediana: {mediana:.1f}')
        
        ax.set_title(f'Distribución de {var}')
        ax.set_xlabel(var)
        ax.set_ylabel('Densidad')
        ax.legend(fontsize=8)
        
        # Agregar texto con asimetría
        asimetria = data.skew()
        ax.text(0.95, 0.95, f'Asimetría: {asimetria:.2f}', 
                transform=ax.transAxes, ha='right', va='top',
                fontsize=9, bbox=dict(boxstyle='round', facecolor='wheat'))
    
    # Ocultar ejes vacíos
    for j in range(i+1, len(axes)):
        axes[j].set_visible(False)
    
    plt.suptitle('Distribución de Variables Numéricas', fontsize=16, y=1.02)
    plt.tight_layout()
    plt.savefig('eda_histogramas.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("\n📊 Interpretación de asimetría:")
    print("  • Asimetría ≈ 0: Distribución simétrica")
    print("  • Asimetría > 0: Cola hacia la derecha (positiva)")
    print("  • Asimetría < 0: Cola hacia la izquierda (negativa)")

plot_histogramas(df_analisis)
```

## 4.2 Boxplots - Detección de Outliers

```python
def plot_boxplots(df, variables=None):
    """
    Boxplots para detectar outliers y comparar distribuciones
    """
    if variables is None:
        variables = ['MENTHLTH', 'PHYSHLTH', 'SLEPTIM1', '_AGE80']
    
    variables = [v for v in variables if v in df.columns]
    
    fig, axes = plt.subplots(1, len(variables), figsize=(4*len(variables), 6))
    if len(variables) == 1:
        axes = [axes]
    
    for i, var in enumerate(variables):
        data = df[var].dropna()
        
        # Boxplot
        bp = axes[i].boxplot(data, patch_artist=True)
        bp['boxes'][0].set_facecolor('lightblue')
        bp['medians'][0].set_color('red')
        bp['medians'][0].set_linewidth(2)
        
        # Calcular outliers
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        outliers = data[(data < Q1 - 1.5*IQR) | (data > Q3 + 1.5*IQR)]
        n_outliers = len(outliers)
        pct_outliers = (n_outliers / len(data)) * 100
        
        axes[i].set_title(f'{var}\n(Outliers: {n_outliers:,} = {pct_outliers:.1f}%)')
        axes[i].set_ylabel('Valor')
        
        # Agregar estadísticos
        stats_text = f'Med: {data.median():.1f}\nIQR: {IQR:.1f}'
        axes[i].text(1.15, data.median(), stats_text, fontsize=9)
    
    plt.suptitle('Boxplots - Distribución y Outliers', fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig('eda_boxplots.png', dpi=150, bbox_inches='tight')
    plt.show()

plot_boxplots(df_analisis)
```

## 4.3 Boxplots Comparativos por Grupos

```python
def plot_boxplots_grupos(df, variable_numerica, variable_grupo, 
                          titulo=None, etiquetas_grupo=None):
    """
    Boxplots comparando una variable numérica entre grupos
    """
    # Preparar datos
    data = df[[variable_numerica, variable_grupo]].dropna()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Crear boxplot
    grupos = sorted(data[variable_grupo].unique())
    data_grupos = [data[data[variable_grupo] == g][variable_numerica] for g in grupos]
    
    bp = ax.boxplot(data_grupos, patch_artist=True)
    
    # Colores
    colores = plt.cm.Set3(np.linspace(0, 1, len(grupos)))
    for patch, color in zip(bp['boxes'], colores):
        patch.set_facecolor(color)
    
    # Etiquetas
    if etiquetas_grupo:
        ax.set_xticklabels([etiquetas_grupo.get(g, str(g)) for g in grupos])
    else:
        ax.set_xticklabels(grupos)
    
    ax.set_ylabel(variable_numerica)
    ax.set_xlabel(variable_grupo)
    
    if titulo:
        ax.set_title(titulo)
    else:
        ax.set_title(f'{variable_numerica} por {variable_grupo}')
    
    # Agregar medias como puntos
    medias = [d.mean() for d in data_grupos]
    ax.scatter(range(1, len(grupos)+1), medias, color='red', s=50, 
               zorder=3, label='Media')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(f'eda_boxplot_{variable_numerica}_por_{variable_grupo}.png', 
                dpi=150, bbox_inches='tight')
    plt.show()
    
    # Estadísticos por grupo
    print(f"\n📊 Estadísticos de {variable_numerica} por {variable_grupo}:")
    stats_grupo = data.groupby(variable_grupo)[variable_numerica].agg(
        ['count', 'mean', 'median', 'std']
    ).round(2)
    print(stats_grupo)

# Ejemplo: Días de mala salud mental por nivel educativo
etiquetas_educ = {1: 'Sin secundaria', 2: 'Secundaria', 
                  3: 'Algo universidad', 4: 'Universitario'}
plot_boxplots_grupos(df_analisis, 'MENTHLTH', '_EDUCAG',
                     titulo='Días de Mala Salud Mental por Nivel Educativo',
                     etiquetas_grupo=etiquetas_educ)

# Ejemplo: Días de mala salud física por sexo
etiquetas_sexo = {1: 'Hombre', 2: 'Mujer'}
plot_boxplots_grupos(df_analisis, 'PHYSHLTH', 'SEX',
                     titulo='Días de Mala Salud Física por Sexo',
                     etiquetas_grupo=etiquetas_sexo)
```

## 4.4 Gráficos de Barras para Variables Categóricas

```python
def plot_barras_categoricas(df, variables=None):
    """
    Gráficos de barras para variables categóricas
    """
    if variables is None:
        variables = ['GENHLTH', '_EDUCAG', '_RFSMOK3', '_TOTINDA']
    
    variables = [v for v in variables if v in df.columns]
    
    # Etiquetas descriptivas
    etiquetas = {
        'GENHLTH': {1: 'Excelente', 2: 'Muy buena', 3: 'Buena', 
                    4: 'Regular', 5: 'Mala'},
        'SEX': {1: 'Hombre', 2: 'Mujer'},
        '_EDUCAG': {1: 'Sin sec.', 2: 'Secundaria', 3: 'Algo univ.', 4: 'Univ.'},
        '_RFSMOK3': {1: 'No fuma', 2: 'Fuma'},
        '_TOTINDA': {1: 'Activo', 2: 'Inactivo'},
        '_RFBING5': {1: 'No', 2: 'Sí'},
        'ADDEPEV2': {1: 'Sí', 2: 'No'}
    }
    
    n_vars = len(variables)
    n_cols = min(2, n_vars)
    n_rows = (n_vars + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6*n_cols, 5*n_rows))
    if n_vars == 1:
        axes = [axes]
    else:
        axes = axes.flatten()
    
    for i, var in enumerate(variables):
        ax = axes[i]
        
        # Calcular frecuencias
        freq = df[var].value_counts().sort_index()
        pct = (freq / freq.sum()) * 100
        
        # Etiquetas
        if var in etiquetas:
            labels = [etiquetas[var].get(idx, str(idx)) for idx in freq.index]
        else:
            labels = [str(idx) for idx in freq.index]
        
        # Gráfico de barras
        bars = ax.bar(labels, pct, color=plt.cm.Pastel1(np.linspace(0, 1, len(freq))),
                      edgecolor='gray')
        
        # Agregar porcentajes encima de las barras
        for bar, p in zip(bars, pct):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                   f'{p:.1f}%', ha='center', va='bottom', fontsize=9)
        
        ax.set_title(f'Distribución de {var}')
        ax.set_ylabel('Porcentaje (%)')
        ax.set_ylim(0, max(pct) * 1.15)
        
        # Rotar etiquetas si son largas
        if max(len(str(l)) for l in labels) > 8:
            ax.tick_params(axis='x', rotation=45)
    
    # Ocultar ejes vacíos
    for j in range(i+1, len(axes)):
        axes[j].set_visible(False)
    
    plt.suptitle('Distribución de Variables Categóricas', fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig('eda_barras_categoricas.png', dpi=150, bbox_inches='tight')
    plt.show()

plot_barras_categoricas(df_analisis)
```

## 4.5 Gráficos de Dispersión (Scatter Plots)

```python
def plot_dispersiones(df, pares_variables=None):
    """
    Gráficos de dispersión para explorar relaciones entre variables
    """
    if pares_variables is None:
        pares_variables = [
            ('_AGE80', 'PHYSHLTH', 'Edad vs Salud Física'),
            ('MENTHLTH', 'PHYSHLTH', 'Salud Mental vs Salud Física'),
            ('SLEPTIM1', 'MENTHLTH', 'Horas de Sueño vs Salud Mental'),
            ('_AGE80', 'SLEPTIM1', 'Edad vs Horas de Sueño')
        ]
    
    # Filtrar pares con variables disponibles
    pares_validos = [(x, y, t) for x, y, t in pares_variables 
                     if x in df.columns and y in df.columns]
    
    n_plots = len(pares_validos)
    n_cols = min(2, n_plots)
    n_rows = (n_plots + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(7*n_cols, 6*n_rows))
    if n_plots == 1:
        axes = [axes]
    else:
        axes = axes.flatten()
    
    for i, (var_x, var_y, titulo) in enumerate(pares_validos):
        ax = axes[i]
        
        # Datos sin missings
        data = df[[var_x, var_y]].dropna()
        
        # Scatter plot con transparencia (muchos puntos)
        ax.scatter(data[var_x], data[var_y], alpha=0.1, s=5, c='steelblue')
        
        # Línea de tendencia (regresión lineal)
        z = np.polyfit(data[var_x], data[var_y], 1)
        p = np.poly1d(z)
        x_line = np.linspace(data[var_x].min(), data[var_x].max(), 100)
        ax.plot(x_line, p(x_line), "r--", linewidth=2, label='Tendencia')
        
        # Correlación
        corr = data[var_x].corr(data[var_y])
        ax.text(0.05, 0.95, f'r = {corr:.3f}', transform=ax.transAxes,
               fontsize=11, verticalalignment='top',
               bbox=dict(boxstyle='round', facecolor='wheat'))
        
        ax.set_xlabel(var_x)
        ax.set_ylabel(var_y)
        ax.set_title(titulo)
        ax.legend()
    
    # Ocultar ejes vacíos
    for j in range(i+1, len(axes)):
        axes[j].set_visible(False)
    
    plt.suptitle('Gráficos de Dispersión - Relaciones entre Variables', 
                 fontsize=14, y=1.02)
    plt.tight_layout()
    plt.savefig('eda_dispersiones.png', dpi=150, bbox_inches='tight')
    plt.show()

plot_dispersiones(df_analisis)
```

## 4.6 Mapa de Calor de Correlaciones

```python
def plot_correlaciones(df, variables=None, metodo='pearson'):
    """
    Mapa de calor de correlaciones entre variables numéricas
    """
    if variables is None:
        variables = ['MENTHLTH', 'PHYSHLTH', 'POORHLTH', '_AGE80', 
                     'SLEPTIM1', '_BMI5']
    
    variables = [v for v in variables if v in df.columns]
    
    # Calcular matriz de correlación
    corr_matrix = df[variables].corr(method=metodo)
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Mapa de calor
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
    
    sns.heatmap(corr_matrix, 
                mask=mask,
                annot=True, 
                fmt='.2f',
                cmap='RdBu_r',
                center=0,
                vmin=-1, vmax=1,
                square=True,
                linewidths=0.5,
                cbar_kws={'shrink': 0.8, 'label': f'Correlación ({metodo})'},
                ax=ax)
    
    ax.set_title(f'Matriz de Correlaciones ({metodo.capitalize()})', fontsize=14)
    
    plt.tight_layout()
    plt.savefig('eda_correlaciones.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # Mostrar correlaciones más fuertes
    print("\n📊 Correlaciones más fuertes (|r| > 0.3):")
    
    corr_pairs = []
    for i in range(len(variables)):
        for j in range(i+1, len(variables)):
            r = corr_matrix.iloc[i, j]
            if abs(r) > 0.3:
                corr_pairs.append((variables[i], variables[j], r))
    
    corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
    
    for var1, var2, r in corr_pairs:
        direccion = "positiva" if r > 0 else "negativa"
        print(f"  • {var1} ↔ {var2}: r = {r:.3f} ({direccion})")
    
    if len(corr_pairs) == 0:
        print("  No se encontraron correlaciones fuertes (|r| > 0.3)")
    
    return corr_matrix

corr_matrix = plot_correlaciones(df_analisis)
```

## 4.7 Pair Plot (Matriz de Dispersiones)

```python
def plot_pairplot(df, variables=None, hue=None):
    """
    Pair plot para visualizar relaciones múltiples
    """
    if variables is None:
        variables = ['MENTHLTH', 'PHYSHLTH', 'SLEPTIM1', '_AGE80']
    
    variables = [v for v in variables if v in df.columns]
    
    # Tomar muestra si el dataset es muy grande
    if len(df) > 5000:
        df_sample = df[variables].dropna().sample(n=5000, random_state=42)
        print(f"📌 Usando muestra de 5,000 observaciones para visualización")
    else:
        df_sample = df[variables].dropna()
    
    # Crear pair plot
    g = sns.pairplot(df_sample, diag_kind='kde', 
                     plot_kws={'alpha': 0.3, 's': 10},
                     diag_kws={'fill': True})
    
    g.fig.suptitle('Pair Plot - Relaciones entre Variables', y=1.02, fontsize=14)
    
    plt.savefig('eda_pairplot.png', dpi=150, bbox_inches='tight')
    plt.show()

plot_pairplot(df_analisis)
```

---

# PASO 5: Análisis Bivariado Específico

## 5.1 Comparación por Grupos (para preguntas de investigación)

```python
def analisis_por_grupos(df, variable_objetivo, variable_grupo, 
                         etiquetas=None, test='auto'):
    """
    Análisis comparativo de una variable entre grupos
    Incluye estadísticos y prueba de hipótesis
    """
    print("="*60)
    print(f"ANÁLISIS: {variable_objetivo} por {variable_grupo}")
    print("="*60)
    
    # Preparar datos
    data = df[[variable_objetivo, variable_grupo]].dropna()
    grupos = sorted(data[variable_grupo].unique())
    
    # Estadísticos por grupo
    stats = data.groupby(variable_grupo)[variable_objetivo].agg([
        'count', 'mean', 'median', 'std', 'min', 'max'
    ]).round(2)
    
    if etiquetas:
        stats.index = [etiquetas.get(g, str(g)) for g in stats.index]
    
    print("\n📊 Estadísticos por grupo:")
    print(stats)
    
    # Prueba estadística
    grupos_data = [data[data[variable_grupo] == g][variable_objetivo] for g in grupos]
    
    if len(grupos) == 2:
        # t-test o Mann-Whitney
        stat_t, p_t = stats.ttest_ind(grupos_data[0], grupos_data[1])
        stat_u, p_u = stats.mannwhitneyu(grupos_data[0], grupos_data[1])
        
        print(f"\n🔬 Pruebas de hipótesis:")
        print(f"  t-test: t = {stat_t:.3f}, p = {p_t:.4f}")
        print(f"  Mann-Whitney U: U = {stat_u:.0f}, p = {p_u:.4f}")
        
    elif len(grupos) > 2:
        # ANOVA o Kruskal-Wallis
        stat_f, p_f = stats.f_oneway(*grupos_data)
        stat_h, p_h = stats.kruskal(*grupos_data)
        
        print(f"\n🔬 Pruebas de hipótesis:")
        print(f"  ANOVA: F = {stat_f:.3f}, p = {p_f:.4f}")
        print(f"  Kruskal-Wallis: H = {stat_h:.3f}, p = {p_h:.4f}")
    
    # Visualización
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Boxplot
    bp = axes[0].boxplot(grupos_data, patch_artist=True)
    colores = plt.cm.Set2(np.linspace(0, 1, len(grupos)))
    for patch, color in zip(bp['boxes'], colores):
        patch.set_facecolor(color)
    
    if etiquetas:
        axes[0].set_xticklabels([etiquetas.get(g, str(g)) for g in grupos])
    else:
        axes[0].set_xticklabels(grupos)
    
    axes[0].set_ylabel(variable_objetivo)
    axes[0].set_title(f'{variable_objetivo} por {variable_grupo}')
    
    # Gráfico de medias con IC
    medias = [d.mean() for d in grupos_data]
    errores = [1.96 * d.std() / np.sqrt(len(d)) for d in grupos_data]
    
    x_pos = range(len(grupos))
    axes[1].bar(x_pos, medias, yerr=errores, capsize=5, 
                color=colores, edgecolor='gray', alpha=0.8)
    
    if etiquetas:
        axes[1].set_xticks(x_pos)
        axes[1].set_xticklabels([etiquetas.get(g, str(g)) for g in grupos])
    
    axes[1].set_ylabel(f'Media de {variable_objetivo}')
    axes[1].set_title('Medias con Intervalo de Confianza 95%')
    
    plt.tight_layout()
    plt.savefig(f'eda_analisis_{variable_objetivo}_por_{variable_grupo}.png', 
                dpi=150, bbox_inches='tight')
    plt.show()

# Ejemplo: Salud mental por sexo
from scipy import stats
analisis_por_grupos(df_analisis, 'MENTHLTH', 'SEX', 
                    etiquetas={1: 'Hombre', 2: 'Mujer'})
```

---

# PASO 6: Dashboard Resumen de EDA

```python
def crear_dashboard_eda(df):
    """
    Crea un dashboard visual resumen del EDA
    """
    fig = plt.figure(figsize=(16, 12))
    
    # Layout: 3 filas x 3 columnas
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 1. Distribución de Salud General
    ax1 = fig.add_subplot(gs[0, 0])
    if 'GENHLTH' in df.columns:
        freq = df['GENHLTH'].value_counts().sort_index()
        etiq = ['Excelente', 'Muy buena', 'Buena', 'Regular', 'Mala']
        colors = ['#2ecc71', '#27ae60', '#f1c40f', '#e67e22', '#e74c3c']
        ax1.bar(etiq, freq.values, color=colors)
        ax1.set_title('Salud General Autopercibida')
        ax1.set_ylabel('Frecuencia')
        ax1.tick_params(axis='x', rotation=45)
    
    # 2. Distribución de Edad
    ax2 = fig.add_subplot(gs[0, 1])
    if '_AGE80' in df.columns:
        df['_AGE80'].hist(bins=30, ax=ax2, color='steelblue', edgecolor='white')
        ax2.axvline(df['_AGE80'].mean(), color='red', linestyle='--', 
                    label=f"Media: {df['_AGE80'].mean():.0f}")
        ax2.set_title('Distribución de Edad')
        ax2.set_xlabel('Edad')
        ax2.legend()
    
    # 3. Días de mala salud mental
    ax3 = fig.add_subplot(gs[0, 2])
    if 'MENTHLTH' in df.columns:
        df['MENTHLTH'].hist(bins=30, ax=ax3, color='purple', 
                           edgecolor='white', alpha=0.7)
        ax3.set_title('Días de Mala Salud Mental')
        ax3.set_xlabel('Días (0-30)')
    
    # 4. Boxplot salud mental por sexo
    ax4 = fig.add_subplot(gs[1, 0])
    if 'MENTHLTH' in df.columns and 'SEX' in df.columns:
        data_h = df[df['SEX'] == 1]['MENTHLTH'].dropna()
        data_m = df[df['SEX'] == 2]['MENTHLTH'].dropna()
        bp = ax4.boxplot([data_h, data_m], patch_artist=True)
        bp['boxes'][0].set_facecolor('lightblue')
        bp['boxes'][1].set_facecolor('lightpink')
        ax4.set_xticklabels(['Hombres', 'Mujeres'])
        ax4.set_title('Salud Mental por Sexo')
        ax4.set_ylabel('Días')
    
    # 5. Prevalencia de comportamientos de riesgo
    ax5 = fig.add_subplot(gs[1, 1])
    riesgos = {}
    if '_RFSMOK3' in df.columns:
        riesgos['Fumador'] = (df['_RFSMOK3'] == 2).mean() * 100
    if '_RFBMI5' in df.columns:
        riesgos['Sobrepeso/Obeso'] = (df['_RFBMI5'] == 2).mean() * 100
    if '_TOTINDA' in df.columns:
        riesgos['Inactivo'] = (df['_TOTINDA'] == 2).mean() * 100
    if '_RFBING5' in df.columns:
        riesgos['Bebe exceso'] = (df['_RFBING5'] == 2).mean() * 100
    
    if riesgos:
        ax5.barh(list(riesgos.keys()), list(riesgos.values()), color='coral')
        ax5.set_xlabel('Porcentaje (%)')
        ax5.set_title('Prevalencia de Factores de Riesgo')
        for i, v in enumerate(riesgos.values()):
            ax5.text(v + 0.5, i, f'{v:.1f}%', va='center')
    
    # 6. Scatter edad vs salud física
    ax6 = fig.add_subplot(gs[1, 2])
    if '_AGE80' in df.columns and 'PHYSHLTH' in df.columns:
        sample = df[['_AGE80', 'PHYSHLTH']].dropna().sample(min(2000, len(df)))
        ax6.scatter(sample['_AGE80'], sample['PHYSHLTH'], alpha=0.2, s=5)
        z = np.polyfit(sample['_AGE80'], sample['PHYSHLTH'], 1)
        p = np.poly1d(z)
        ax6.plot(sample['_AGE80'].sort_values(), 
                p(sample['_AGE80'].sort_values()), 'r--')
        ax6.set_xlabel('Edad')
        ax6.set_ylabel('Días mala salud física')
        ax6.set_title('Edad vs Salud Física')
    
    # 7. Correlaciones (mini heatmap)
    ax7 = fig.add_subplot(gs[2, 0:2])
    vars_corr = ['MENTHLTH', 'PHYSHLTH', 'POORHLTH', '_AGE80', 'SLEPTIM1']
    vars_corr = [v for v in vars_corr if v in df.columns]
    if len(vars_corr) > 2:
        corr = df[vars_corr].corr()
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r', 
                    center=0, ax=ax7, cbar_kws={'shrink': 0.8})
        ax7.set_title('Matriz de Correlaciones')
    
    # 8. Resumen de muestra
    ax8 = fig.add_subplot(gs[2, 2])
    ax8.axis('off')
    resumen_texto = f"""
    RESUMEN DEL DATASET
    
    N total: {len(df):,}
    
    Variables analizadas: {len(df.columns)}
    
    Período: BRFSS 2022
    
    Fuente: CDC
    """
    ax8.text(0.1, 0.5, resumen_texto, fontsize=12, 
             verticalalignment='center', family='monospace',
             bbox=dict(boxstyle='round', facecolor='lightyellow'))
    
    plt.suptitle('Dashboard de Análisis Exploratorio - BRFSS', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    plt.savefig('eda_dashboard_resumen.png', dpi=150, bbox_inches='tight')
    plt.show()

crear_dashboard_eda(df_analisis)
```

---

# PASO 7: Discusión de Hallazgos

```python
def generar_discusion(df, preguntas_investigacion):
    """
    Genera una discusión estructurada de los hallazgos del EDA
    relacionándolos con las preguntas de investigación
    """
    print("="*70)
    print("DISCUSIÓN DE HALLAZGOS DEL EDA")
    print("="*70)
    
    for i, pregunta in enumerate(preguntas_investigacion, 1):
        print(f"\n{'─'*70}")
        print(f"PREGUNTA {i}: {pregunta['texto']}")
        print(f"{'─'*70}")
        
        print(f"\n📊 Variables relevantes: {', '.join(pregunta['variables'])}")
        
        print(f"\n📈 Hallazgos descriptivos:")
        for hallazgo in pregunta['hallazgos']:
            print(f"   • {hallazgo}")
        
        print(f"\n🔍 Implicaciones para el análisis:")
        for implicacion in pregunta['implicaciones']:
            print(f"   → {implicacion}")

# Ejemplo de uso
preguntas = [
    {
        'texto': '¿Existe relación entre la salud mental y la salud física?',
        'variables': ['MENTHLTH', 'PHYSHLTH', 'POORHLTH'],
        'hallazgos': [
            'Correlación positiva moderada entre MENTHLTH y PHYSHLTH (r = 0.45)',
            'El 15% de la muestra reporta más de 14 días de mala salud mental',
            'La distribución de ambas variables tiene asimetría positiva (cola derecha)'
        ],
        'implicaciones': [
            'Aplicar regresión para cuantificar la relación',
            'Considerar transformación logarítmica por asimetría',
            'Posible bidireccionalidad: explorar con modelos estructurales'
        ]
    },
    {
        'texto': '¿Difieren los comportamientos de salud entre grupos educativos?',
        'variables': ['_EDUCAG', '_RFSMOK3', '_RFBMI5', '_TOTINDA'],
        'hallazgos': [
            'Mayor proporción de fumadores en nivel educativo bajo (25% vs 8%)',
            'Obesidad más prevalente en niveles educativos bajos',
            'Inactividad física disminuye con mayor educación'
        ],
        'implicaciones': [
            'Usar chi-cuadrado para confirmar asociaciones',
            'Aplicar regresión logística controlando por edad e ingreso',
            'Considerar clustering para identificar perfiles de riesgo'
        ]
    }
]

generar_discusion(df_analisis, preguntas)
```

---

# Estructura Sugerida para el Notebook

```markdown
## NOTEBOOK: Análisis Exploratorio de Datos

### 1. Introducción y Carga de Datos
- Descripción del dataset BRFSS
- Carga y vista preliminar
- Preguntas de investigación

### 2. Exploración Inicial
- Dimensiones y tipos de datos
- Selección de variables relevantes
- Análisis de valores faltantes

### 3. Estadísticos Descriptivos
- Variables numéricas: media, mediana, desv. std, cuartiles
- Variables categóricas: frecuencias y porcentajes
- Resumen ejecutivo de la muestra

### 4. Visualizaciones
- Histogramas de variables numéricas
- Boxplots para detección de outliers
- Gráficos de barras para categóricas
- Scatter plots para relaciones
- Mapa de calor de correlaciones

### 5. Análisis Bivariado
- Comparaciones por grupos relevantes
- Tablas cruzadas para categóricas
- Correlaciones significativas

### 6. Discusión de Hallazgos
- Relación con preguntas de investigación
- Patrones identificados
- Implicaciones para análisis posteriores

### 7. Conclusiones del EDA
- Resumen de hallazgos principales
- Variables clave identificadas
- Preparación para técnicas estadísticas
```

---

*Documento generado para proyecto de Estadística - Universidad de La Habana, MATCOM*
