# AI Document Generator Architecture

## 1) System architecture

The platform uses a modular layered architecture:

1. **Presentation layer (Next.js frontend)**: prompt form, type selector, editor, version browser, and export actions.
2. **API layer (FastAPI routes)**: JWT-protected endpoints for auth, generation, and document CRUD.
3. **Service layer**: orchestration for generation, templates, formatting, versioning, and export.
4. **AI generation layer**: prompt builder, outline generator, and section generator abstraction for OpenAI/local LLM.
5. **Document builder layer**: merges generated sections with template-driven structure.
6. **PDF rendering layer**: HTML/LaTeX conversion and PDF export pipeline.
7. **Storage layer**: PostgreSQL metadata + object storage for PDF artifacts.

### Data flow

Prompt -> Generation config -> AI outline -> Section content -> Formatter -> Persist draft -> Render PDF -> Store file URL -> Return document record.

## 2) File structure

```text
/app
  /frontend
    /components
    /pages
    /editor
    /templates
    /styles
  /backend
    main.py
    config.py
    /api
      routes_documents.py
      routes_generation.py
      routes_user.py
      deps.py
    /services
      ai_service.py
      document_service.py
      template_service.py
      pdf_service.py
    /models
      base.py
      user_model.py
      document_model.py
      template_model.py
    /schemas
      document_schema.py
      user_schema.py
    /repositories
      document_repository.py
      user_repository.py
    /utils
      db.py
      security.py
      text_formatter.py
      pdf_utils.py
  /ai
    prompt_builder.py
    section_generator.py
    outline_generator.py
  /templates
    dissertation_template.json
    report_template.json
    essay_template.json
  /pdf
    /latex_templates
    pdf_renderer.py
/tests
  test_generation.py
  test_pdf.py
```

## 3) Module responsibilities

- `routes_user.py`: registration/login and token issuance.
- `routes_generation.py`: protected generation endpoint.
- `routes_documents.py`: list/update + version increment.
- `document_service.py`: pipeline orchestration from prompt to PDF.
- `ai_service.py`: LLM abstraction and deterministic local fallback.
- `template_service.py`: load type-based section templates.
- `pdf_service.py` + `pdf_renderer.py`: format and render PDF artifact.
- `repositories/*`: persistence boundary for users/documents.
- `schemas/*`: API contracts with validation.
- `models/*`: relational entity definitions.
- `utils/security.py`: password hashing and JWT lifecycle.
- `utils/db.py`: SQLAlchemy engine/session management.
