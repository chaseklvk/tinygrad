from tinygrad.device import Compiled, LRUAllocator, Compiler, CompilerOptions
from tinygrad.renderer.assembly import TinyRenderer
import functools
from typing import Any

class TinyCoreDevice(Compiled):
  def __init__(self, device:str):
    super().__init__("TINYCORE", TinyCoreAllocator(self), TinyCoreCompiler(self), functools.partial(TinyCoreProgram, self))

class TinyCoreCompiler(Compiler):
  compiler_opts = CompilerOptions("TINYCORE")
  def __init__(self, device:TinyCoreDevice):
    super().__init__("compile_tinycore")
  
  def render(self, name: str, uops) -> str: return TinyRenderer(name, uops)
  def compile(self, src:str) -> bytes:
    print(f"compile, {src}")

class TinyCoreAllocator(LRUAllocator):
  def __init__(self, device:TinyCoreDevice):
    super().__init__()
  
  def _alloc(self, size:int, options) -> Any:
    print(f"_alloc, {size}, {options}")
  
  def copyin(self, dest:Any, src:memoryview):
    print(f"copyin, {dest}, {src}")

class TinyCoreProgram:
  def __init__(self, device:TinyCoreDevice):
    print("in tinycore program")
  
  def __call__(self):
    print("calling tinycore program")