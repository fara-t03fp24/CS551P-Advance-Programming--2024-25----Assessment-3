def test_index_page(client):
    """Test the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Cybersecurity Events Dashboard' in response.data
    assert b'Recent Events' in response.data

def test_event_detail_page(client):
    """Test the event detail page loads correctly."""
    response = client.get('/event/TEST001')
    assert response.status_code == 200
    assert b'Event Details' in response.data
    assert b'SQL Injection' in response.data
    assert b'Test Intelligence' in response.data

def test_event_detail_not_found(client):
    """Test 404 error for non-existent event."""
    response = client.get('/event/NONEXISTENT')
    assert response.status_code == 404

def test_analysis_page(client):
    """Test the analysis page loads correctly."""
    response = client.get('/analysis')
    assert response.status_code == 200
    assert b'Attack Analysis' in response.data
    assert b'Attack Type Distribution' in response.data
    assert b'Severity Distribution' in response.data