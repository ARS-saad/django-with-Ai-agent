from documents.models import Document
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig

@tool
def list_documents(config: RunnableConfig):
    """
    Get documents for the current user.
    """
    metadata = config.get('metadata') or config.get('configurable')
    user_id = metadata.get('user_id')  # type: ignore
    if user_id is None:
        raise Exception("User id is not found")
    qs = Document.objects.filter(active=True) # type: ignore
    response_data = []
    for obj in qs:
        response_data.append(
            {
                "id": obj.id,
                "title": obj.title
            }
        )

    return response_data

@tool
def get_document(document_id: int, config: RunnableConfig):
    """
    Get the details of a document for the current user.
    """
    metadata = config.get('metadata') or config.get('configurable')
    user_id = metadata.get('user_id')  # type: ignore
    if user_id is None:
        raise Exception("User id is not found")
    try:
        obj = Document.objects.get(id=document_id, owner_id = user_id, active=True) # type: ignore
    except Document.DoesNotExist:   # type: ignore
        raise Exception("Document is not found")
    except:
        raise Exception("Invalid request for document")
    print(config)
    response_data = {
        "id": obj.id,
        "title": obj.title
    }

    return response_data
