# Pygbag Troubleshooting Guide

## Black Screen / App Not Loading

### Symptom
After clicking "ready to start" in the browser, you see only a black rectangle instead of your pygame application.

### Common Causes and Solutions

#### 1. Silent Packaging Failure (Most Common on Windows)
**Problem**: Pygbag encounters an error during packaging but doesn't clearly report it, resulting in incomplete builds. On Windows, temporary files like `nul` can cause the packing process to fail silently, showing "packing 1 files complete" instead of the correct number of files.

**How to Diagnose**:
- Check the build output for the line "packing X files complete"
- Count your expected files: main.py + other .py files + images + other assets
- If X is much lower than expected, you have a packaging failure

**Solution**:
```bash
# Clean everything and rebuild
rm -rf build
rm -f nul  # Remove Windows temp file if it exists
python -m pygbag --build .
```

After rebuild, verify the packaging:
```bash
python -c "import zipfile; z = zipfile.ZipFile('build/web/YOURAPP.apk'); print('\n'.join(z.namelist()))"
```

All your Python files and assets should be listed under the `assets/` directory.

#### 2. Images Not Found
**Problem**: Image files aren't being loaded, causing the app to crash silently.

**Solution**:
- Place images in a subfolder (e.g., `assets/`, `graphics/`, `Graphics/`)
- Use lowercase paths in your code: `pygame.image.load('assets/image.png')`
- After moving files, always do a clean rebuild: `rm -rf build && python -m pygbag --build .`

#### 3. Module Import Issues
**Problem**: Importing from local modules can sometimes trigger pygbag to download packages from PyPI with the same name.

**Diagnosis**: Check browser console for messages like "Begin.cross_file.fetch https://pypi.org/simple/MODULENAME/"

**Solution**:
- Use clean builds: `rm -rf build` before rebuilding
- If a local module name conflicts with a PyPI package, consider renaming your module
- Verify your .py files are included in the package (see diagnostic command above)

### General Debugging Steps

1. **Always check the browser console** (F12) for Python errors or loading issues
2. **Verify package contents** after each build to ensure all files are included
3. **Do clean rebuilds** when making structural changes (new files, moved assets)
4. **Test locally first** before deploying to GitHub Pages

### Quick Checklist Before Deploying
- [ ] Clean build completed: `rm -rf build && python -m pygbag --build .`
- [ ] Packaging shows correct file count
- [ ] Package contents verified with zipfile command
- [ ] App works at http://localhost:8000
- [ ] Browser console shows no errors
