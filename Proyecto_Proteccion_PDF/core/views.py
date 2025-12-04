import io
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Por ahora es un stub sencillo:
# - health_check: para probar que el servicio está vivo
# - proteger_pdf: recibe un PDF y lo devuelve igual (luego metemos la lógica avanzada)


def health_check(request):
    return JsonResponse({"status": "ok", "message": "Proteccion_PDF activo"})


@csrf_exempt  # Power Automate generalmente llama sin CSRF token
def proteger_pdf(request):
    if request.method != "POST":
        return JsonResponse({"error": "Solo se permite POST"}, status=405)

    if "pdf" not in request.FILES:
        return JsonResponse({"error": "No se recibió ningún archivo 'pdf'"}, status=400)

    uploaded_file = request.FILES["pdf"]

    # TODO: Aquí luego metemos la lógica REAL de protección (Ghostscript / imágenes, etc.)
    # Por ahora solo devolvemos el mismo PDF para tener el flujo completo funcionando.

    pdf_bytes = uploaded_file.read()
    buffer = io.BytesIO(pdf_bytes)

    response = HttpResponse(
        buffer.getvalue(),
        content_type="application/pdf",
    )
    response["Content-Disposition"] = 'attachment; filename="pdf_protegido.pdf"'
    return response
