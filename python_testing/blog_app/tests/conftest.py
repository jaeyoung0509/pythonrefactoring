import os
import tempfile
from fastapi import testclient
import pytest
from blog.models import Article

@pytest.fixture(autouse= True)
def database():
    _ , file_name = tempfile.mkdtemp()
    os.environ["DATABASE_NAME"] = file_name
    Article.create_table(database_name=file_name)
    yield
    os.unlink(file_name)