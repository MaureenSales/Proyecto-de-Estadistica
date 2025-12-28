# 📊 Análisis Estadístico sobre la Violencia de Género 

## 📋 Objetivos: 

Analizar estadísticamente patrones de violencia de género y violencia doméstica considerando víctimas y perpetradores de ambos sexos, para identificar: 

- que indicadores (ej: tipo de abuso) predominan por género.
- qué grupos etarios son más sensibles según tipo de violencia.
- diferencias por región/urbano-rural y por variables socioeconómicas.
- construir modelos predictivos y de segmentación (clustering) para caracterizar perfiles de riesgo
- evaluación de  posibles coorelaciones (ej: relación con el agresor)

---

## 📌 Variables 
- Sexo de la víctima(M\F)
- Sexo del perpetrador (M\F)
- Edad de la víctima
- Edad del perpetrador
- Fecha del evento
- Tipo de violencia (física, sexual, psicológica, económica)
- Homicidio (sí/no)
- Grado del evento
- Relación perpetrador-víctima
- Lugar (país, región, urbano\rural)
- Datos socioeconómicos de la víctima
- Fuente

---

## 📁 Repositorios Confiables


1. ***UN Women – Global Database on Violence against Women and Girls***: estadísticas por país sobre violencia de pareja, no pareja, prácticas nocivas (FGM, matrimonio forzado). Útil para prevalencias poblacionales y series por país, cifras y tendencias recientes sobre feminicidio y homicidios por pareja

2. ***WHO (World Health Organization) — Violence indicators / intimate partner violence prevalence***: estimaciones globales y series por edad/región. Ideal para prevalencia y comparaciones regionales.

3. ***UNODC — Homicide statistics (victims disaggregated by sex and age)***: base de datos de homicidios intencionales con desagregación por sexo y edad; fundamental para analizar homicidios por género.

4. ***World Bank / Gender Data Portal***: indicadores de violencia, datos relacionados y meta-información. Buen punto de partida para juntar indicadores socioeconómicos.

5. ***PAHO / WHO regional (Región de las Américas)***: estimados regionales y hojas técnicas por país (útil para analizar países americanos)

6. ***FRA (European Union Agency for Fundamental Rights) — Violence against women survey (EU-wide)***: encuesta representativa (42k mujeres) con datos por edad, lugar, agresor y contexto. Útil para análisis detallado en países UE.

7. ***VAW Data / Global estimates interactive (Harvard/partners)*** — base con estimaciones de violencia pareja/no pareja

8. ***data.europa.eu / data portals nacionales (Open Data)***: para descargar datasets nacionales sobre violencia y registros policiales.

### 🔄 Idea Plan de Trabajo

1. Recolectar datasets principales

2. Exploratory Data Analysis (EDA)
- Limpieza: unificar formatos de fecha, codificar sexos, agrupar edades.
- Estadísticos descriptivos
- Visualizacioones

3. Crear variables derivadas: tasa por 100k, indicador severidad, indicador pareja_vs_no_pareja.

4. Pruebas de hipótesis
   - t-test / Mann-Whitney: diferencia de edad media entre víctimas M vs F para cada tipo de violencia
   - Chi-cuadrado: asociación entre sexo de víctima y tipo de agresor.

5. Regresión
- Regresión logística (binary): p.ej. probabilidad de homicidio dado sexo, edad, relación agresor, región.
- Regresión Poisson o tasa (si modelas conteos/homicidios por región).

6. Reducir dimensionalidad de variables socioeconómicas y comportamiento para visualizaciones.

7. Clustering (K-Means / Hierarchical / DBSCAN)
- Identificar perfiles de víctimas (edad, tipo de abuso, severidad, reporte). Interpretar clusters (perfiles de riesgo).

8. Resultados y validación
- Interpretación: responde preguntas de investigación con evidencia estadística (intervalos de confianza, p-values, efectos).
- Validación y análisis de sesgos.

---
## 🔎 Sugerencias

#### 1. ¿Qué tipos predominan por género? → tablas de contingencia + chi-cuadrado + gráficos de barras apiladas.

#### 2. ¿Grupos etarios más sensibles? → tasas por 100k por grupo etario; ANOVA / Kruskal-Wallis para diferencias entre grupos.

#### 3. ¿Indicadores que predicen homicidio? → regresión logística o Poisson (si modelas conteos por área). Incluir interacción sexo×edad.