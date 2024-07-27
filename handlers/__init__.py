from .employee import router as employee_router
from .instructions import router as instructions_router
from .start import router as start_router


routers = [start_router, employee_router, instructions_router, ]
