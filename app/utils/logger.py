"""
Simple logging setup for the cybersecurity tracker
Student ID: [Your ID]
May 17, 2025
"""
import logging
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
log_dir = Path(__file__).parent.parent.parent / 'logs'
log_dir.mkdir(exist_ok=True)

# Configure the logger
def setup_logger(name='cybersecurity_tracker'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Log format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # File handler - keeps rotating log files
    file_handler = RotatingFileHandler(
        log_dir / 'app.log',
        maxBytes=1024 * 1024,  # 1MB per file
        backupCount=10  # Keep 10 backup files
    )
    file_handler.setFormatter(formatter)
    
    # Console handler for development
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Add handlers if they haven't been added already
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# Create default logger instance
logger = setup_logger()