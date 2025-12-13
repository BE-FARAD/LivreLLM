import pytest
from pathlib import Path
from src.input.file_watcher import FileWatcher

def test_scan_directory(tmp_path):
    # Setup
    d = tmp_path / "input"
    d.mkdir()
    p = d / "test.pdf"
    p.write_text("fake pdf content")
    
    watcher = FileWatcher(input_directory=d)
    files = watcher.scan_directory()
    
    assert len(files) == 1
    assert files[0].name == "test.pdf"

def test_compute_hash(tmp_path):
    d = tmp_path / "input"
    d.mkdir()
    p = d / "test.pdf"
    content = b"test content"
    p.write_bytes(content)
    
    watcher = FileWatcher(input_directory=d)
    h = watcher.compute_hash(p)
    
    # sha256 of "test content"
    # echo -n "test content" | shasum -a 256
    # 6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72
    assert h == "6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72"

def test_validate_pdf(tmp_path):
    d = tmp_path / "input"
    d.mkdir()
    
    valid = d / "valid.pdf"
    valid.write_bytes(b"content")
    
    invalid_ext = d / "test.txt"
    invalid_ext.write_bytes(b"content")
    
    empty = d / "empty.pdf"
    empty.touch()
    
    watcher = FileWatcher(input_directory=d)
    
    assert watcher.validate_pdf(valid) == True
    assert watcher.validate_pdf(invalid_ext) == False
    assert watcher.validate_pdf(empty) == False
