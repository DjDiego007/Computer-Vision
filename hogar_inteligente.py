import cv2
import time

# Configuración del modelo: Uso de Haar Cascades para detección frontal de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicialización de hardware (Cámara Kuiiyer)
# Se utiliza el índice 1 para cámara externa; cambiar a 0 si es integrada
cap = cv2.VideoCapture(1)

# Tiempo de espera para estabilización del sensor de imagen
time.sleep(2)

print("--- SISTEMA DE GESTIÓN DE HOGAR INTELIGENTE ACTIVO ---")
print("Estado: Monitoreando acceso principal. Presione 'q' para finalizar.")

while True:
    # Captura de frame por frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error crítico: No se detecta flujo de video de la cámara.")
        break

    # Preprocesamiento: Conversión a escala de grises para optimizar la detección
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detección de rostros con parámetros ajustados para reducir falsos positivos
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.2, 
        minNeighbors=5, 
        minSize=(50, 50)
    )

    # Lógica de respuesta del sistema ante detección
    if len(faces) > 0:
        # Acción simulada de Domótica
        print("EVENTO: Rostro identificado. Ejecutando protocolo 'Bienvenida':")
        print("  > Luces de estancia: ON (Cálido)")
        print("  > Reproduciendo: Playlist Relajación")
        
        # Implementación de feedback visual en el stream de video
        for (x, y, w, h) in faces:
            # Dibujar rectángulo de detección (Verde BGR: 0, 255, 0)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(frame, 'USUARIO DETECTADO', (x, y-10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Generación de evidencia automática para el reporte
        cv2.imwrite('evidencia_rostro.jpg', frame)

    # Despliegue de la interfaz de monitoreo
    cv2.imshow('Monitor de Seguridad - Home AI', frame)

    # Salida controlada del sistema
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Cerrando sistema...")
        break

# Liberación de recursos de hardware y cierre de ventanas
cap.release()
cv2.destroyAllWindows()