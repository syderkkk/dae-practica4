from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Student

def student_list(request):
    # Obtener parámetro de búsqueda
    search_query = request.GET.get('search', '')
    
    # Filtrar estudiantes activos
    students = Student.objects.filter(is_active=True)
    
    # Aplicar búsqueda si existe
    if search_query:
        students = students.filter(
            first_name__icontains=search_query
        ) | students.filter(
            last_name__icontains=search_query
        )
    
    # Ordenar por apellido
    students = students.order_by('last_name', 'first_name')
    
    # Paginación
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'students': page_obj,
        'search_query': search_query,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, 'students/student_list.html', context)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        student_id = request.POST.get('student_id')
        career = request.POST.get('career')
        semester = request.POST.get('semester')
        phone = request.POST.get('phone')
        birth_date = request.POST.get('birth_date')
        
        # Crear el estudiante
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            student_id=student_id,
            career=career,
            semester=semester,
            phone=phone,
            birth_date=birth_date if birth_date else None
        )
        
        messages.success(request, 'Estudiante creado exitosamente.')
        return redirect('student_list')
    
    return render(request, 'students/student_form.html')

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        # Actualizar datos
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.student_id = request.POST.get('student_id')
        student.career = request.POST.get('career')
        student.semester = request.POST.get('semester')
        student.phone = request.POST.get('phone')
        birth_date = request.POST.get('birth_date')
        student.birth_date = birth_date if birth_date else None
        student.is_active = 'is_active' in request.POST
        
        student.save()
        
        messages.success(request, 'Estudiante actualizado exitosamente.')
        return redirect('student_list')
    
    return render(request, 'students/student_form.html', {'object': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Estudiante eliminado exitosamente.')
        return redirect('student_list')
    
    return render(request, 'students/student_confirm_delete.html', {'student': student})