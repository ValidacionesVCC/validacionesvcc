from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import os
import tempfile
import subprocess

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader


# -------------------------------------
# Vista principal (pantalla de inicio)
# -------------------------------------
def inicio_view(request):
    return render(request, 'core/inicio.html')


# -------------------------------------
# API: Convertir PDF en PDF hecho de imágenes
# -------------------------------------
@csrf_exempt
def convertir_pdf_en_imagenes_pdf(request):
    """
    Convierte cada página del PDF recibido en una imagen
    y genera un nuevo PDF solo con imágenes (NO seleccionable).
    """
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido. Usa POST."}, status=405)

    if request.content_type != "application/pdf":
        return JsonResponse({"error": "Content-Type debe ser application/pdf"}, status=400)

    pdf_bytes = request.body
    if not pdf_bytes:
        return JsonResponse({"error": "No se recibió ningún PDF"}, status=400)


    with tempfile.TemporaryDirectory() as tmpdir:

        input_pdf = os.path.join(tmpdir, "entrada.pdf")
        with open(input_pdf, "wb") as f:
            f.write(pdf_bytes)

        output_pattern = os.path.join(tmpdir, "pagina-%04d.png")

        gs_cmd = [
            "gs",
            "-dSAFER",
            "-dBATCH",
            "-dNOPAUSE",
            "-sDEVICE=png16m",
            "-r200",
            f"-sOutputFile={output_pattern}",
            input_pdf,
        ]

        try:
            subprocess.check_call(gs_cmd)
        except Exception as e:
            return JsonResponse(
                {"error": "Ghostscript falló", "detalle": str(e)}, status=500
            )

        pages = sorted([p for p in os.listdir(tmpdir) if p.endswith(".png")])

        if not pages:
            return JsonResponse({"error": "No se generaron imágenes"}, status=500)

        salida_pdf = os.path.join(tmpdir, "salida.pdf")
        c = canvas.Canvas(salida_pdf, pagesize=A4)
        width, height = A4

        for img_name in pages:
            img_path = os.path.join(tmpdir, img_name)
            img = ImageReader(img_path)

            iw, ih = img.getSize()
            r = min(width / iw, height / ih)
            new_w = iw * r
            new_h = ih * r
            x = (width - new_w) / 2
            y = (height - new_h) / 2

            c.drawImage(img, x, y, new_w, new_h)
            c.showPage()

        c.save()

        with open(salida_pdf, "rb") as f:
            final_bytes = f.read()

    response = HttpResponse(final_bytes, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="pdf_solo_imagenes.pdf"'
    return response
