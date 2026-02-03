# Ideas de Tests para Ingeniero de Datos
Basado en el JSON del CRM, aquí hay tests que podrías escribir:

## 📊 Tests de Transformación de Datos

### Extracción y Limpieza
- [ ] Extraer todos los emails de clientes
- [ ] Extraer nombres completos (first_name + last_name)
- [ ] Extraer lista de industrias únicas
- [ ] Extraer fechas de última compra
- [ ] Limpiar/validar formato de teléfonos
- [ ] Validar que emails tengan formato correcto

### Cálculos y Agregaciones
- [ ] Calcular lifetime_value promedio
- [ ] Calcular total de compras por cliente
- [ ] Calcular edad promedio de clientes
- [ ] Sumar revenue total por tier (bronze, silver, gold, platinum)
- [ ] Calcular promedio de loyalty_points por tier
- [ ] Contar clientes por estado/ciudad

### Transformaciones
- [ ] Convertir fecha de nacimiento a edad
- [ ] Agrupar clientes por industria
- [ ] Agrupar clientes por rango de LTV (0-20k, 20k-50k, 50k+)
- [ ] Crear resumen con solo campos esenciales
- [ ] Convertir estructura anidada a plana
- [ ] Normalizar nombres de estados/ciudades

### Enriquecimiento
- [ ] Agregar segmento según LTV (premium/standard/basic)
- [ ] Agregar categoría de frecuencia según total_purchases
- [ ] Agregar flag de "cliente activo" según last_purchase_date
- [ ] Agregar días desde última compra
- [ ] Calcular percentil de cada cliente en LTV

## 🔍 Tests de Filtrado

### Por Status y Estado
- [ ] Filtrar clientes activos vs inactivos vs churned
- [ ] Filtrar por tier de lealtad
- [ ] Filtrar por estado geográfico
- [ ] Filtrar por país
- [ ] Filtrar por tamaño de empresa

### Por Valores Numéricos
- [ ] Filtrar por lifetime_value > X
- [ ] Filtrar por rango de LTV (min, max)
- [ ] Filtrar por total_purchases > X
- [ ] Filtrar por loyalty_points > X
- [ ] Filtrar por revenue de empresa > X
- [ ] Filtrar por edad (mayor/menor que X)

### Por Categorías y Tags
- [ ] Filtrar por industria específica
- [ ] Filtrar clientes con tag 'vip'
- [ ] Filtrar clientes con tag 'inactive-risk'
- [ ] Filtrar por canal de comunicación preferido
- [ ] Filtrar por idioma
- [ ] Filtrar por múltiples tags

### Por Fechas
- [ ] Filtrar clientes con compras en últimos 30 días
- [ ] Filtrar clientes que NO compraron en 60+ días
- [ ] Filtrar por año de registro (created_at)
- [ ] Filtrar clientes registrados en 2024 vs 2025

### Por Consentimientos
- [ ] Filtrar con marketing_consent = true
- [ ] Filtrar suscritos a newsletter
- [ ] Filtrar con ambos consentimientos

### Filtros Complejos (Combinados)
- [ ] Clientes VIP + activos + LTV > 50k
- [ ] Clientes de Technology + tier platinum
- [ ] Clientes inactivos sin marketing_consent
- [ ] Clientes de CDMX + alta frecuencia de compra
- [ ] SMBs (10-50 employees) con alto LTV

## 📈 Tests de Validación de Datos

### Integridad
- [ ] Verificar que no hay IDs duplicados
- [ ] Verificar que todos tienen email
- [ ] Verificar que LTV >= 0
- [ ] Verificar que total_purchases >= 0
- [ ] Verificar formato de fechas (ISO 8601)

### Consistencia
- [ ] Tier corresponde al rango de loyalty_points
- [ ] Status 'churned' no tiene compras recientes
- [ ] last_purchase_date <= fecha actual
- [ ] created_at <= updated_at

### Completitud
- [ ] Todos los clientes tienen campos requeridos
- [ ] No hay valores None/null en campos críticos
- [ ] Arrays de tags no están vacíos

## 🎯 Tests de Casos Edge

- [ ] Manejar lista vacía de clientes
- [ ] Buscar cliente que no existe (debe retornar None)
- [ ] Filtrar con criterio que no devuelve resultados
- [ ] Calcular promedio con 0 clientes
- [ ] Ordenar por campo con valores iguales

## 📦 Tests de Integración

- [ ] Cargar JSON y extraer todos los emails
- [ ] Pipeline completo: cargar → filtrar → transformar → agrupar
- [ ] Generar reporte con múltiples métricas
- [ ] Exportar datos filtrados a nuevo JSON

## 💡 Tests de Lógica de Negocio

### Segmentación
- [ ] Identificar top 10% de clientes por LTV
- [ ] Identificar clientes en riesgo de churn
- [ ] Segmentar por recency/frequency/monetary (RFM)

### Análisis
- [ ] Calcular tasa de retención por tier
- [ ] Identificar industrias más rentables
- [ ] Calcular LTV promedio por canal de comunicación

---
