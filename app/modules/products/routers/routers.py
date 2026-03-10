from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import FileResponse
from pathlib import Path
import json
from app.modules.products.services.services import get_all_products, get_product_by_id
from app.modules.auth.bearer import verify_token

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


def build_absolute_urls(data, base_url):
    """Convert relative URLs to absolute URLs in the response data."""
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "url" and isinstance(value, str) and value.startswith("/"):
                data[key] = f"{base_url}{value}"
            elif isinstance(value, (dict, list)):
                build_absolute_urls(value, base_url)
    elif isinstance(data, list):
        for item in data:
            build_absolute_urls(item, base_url)
    return data


@router.get("/download/metadata/{metadata_id}")
def download_metadata(metadata_id: int):
    """Download metadata file by metadata_id."""
    file_path = Path(__file__).resolve().parent.parent.parent.parent / "public" / "data" / "metadata" / f"{metadata_id}.json"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Metadata not found")
    return FileResponse(
        path=file_path, 
        media_type='application/octet-stream',
        filename=f'metadata_{metadata_id}.json'
    )


@router.get("/")
def getProducts(request: Request, token: str = Depends(verify_token)):
    products = get_all_products()
    base_url = f"{request.url.scheme}://{request.url.netloc}"
    return build_absolute_urls(products, base_url)


@router.get("/{product_id}")
def getProductsById(product_id: int, request: Request, token: str = Depends(verify_token)):
    product = get_product_by_id(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    base_url = f"{request.url.scheme}://{request.url.netloc}"
    return build_absolute_urls(product, base_url)
