"""
Input
"""

import pygame

def _trigger_input() -> bool:
    if (pygame.event.peek(pygame.KEYDOWN)):
        return True
    return False