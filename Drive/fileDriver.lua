
function main()
    renderPath = getRenderPath()
end

function getRenderPath()
    projectPath = reaper.GetProjectPathEx( 0, "")
    nope ,exportName = reaper.GetSetProjectInfo_String(0, "RENDER_FILE", " ", false)
    fullPath = projectPath .. "\\" .. exportName
    print(fullPath)
end

function setRenderSettings()
end

function print(toPrint)
    reaper.ShowConsoleMsg(toPrint)
end

main()
