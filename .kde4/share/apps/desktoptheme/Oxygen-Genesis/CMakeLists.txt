
install(FILES colors metadata.desktop DESTINATION ${DATA_INSTALL_DIR}/desktoptheme/Oxygen-Genesis/)

FILE(GLOB widgets widgets/*.svg*)
install( FILES ${widgets} DESTINATION ${DATA_INSTALL_DIR}/desktoptheme/Oxygen-Genesis/widgets/ )

FILE(GLOB dialogs dialogs/*.svgz)
install( FILES ${dialogs} DESTINATION ${DATA_INSTALL_DIR}/desktoptheme/Oxygen-Genesis/dialogs/ )

FILE(GLOB icons icons/*.svgz)
install( FILES ${icons} DESTINATION ${DATA_INSTALL_DIR}/desktoptheme/Oxygen-Genesis/icons/ )

FILE(GLOB lancelot lancelot/*.*)
install( FILES ${lancelot} DESTINATION ${DATA_INSTALL_DIR}/desktoptheme/Oxygen-Genesis/lancelot/ )

FILE(GLOB opaque opaque/widgets/*.svg*)
install( FILES ${opaque} DESTINATION ${DATA_INSTALL_DIR}/desktoptheme/Oxygen-Genesis/opaque/widgets/ )

FILE(GLOB opaque opaque/dialogs/*.svg*)
install( FILES ${opaque} DESTINATION ${DATA_INSTALL_DIR}/desktoptheme/Oxygen-Genesis/opaque/dialogs/ )

