def test_capturemessage_react_native_ios(ios_react_native_sim_driver):
    # click on list app
    ios_react_native_sim_driver.find_element_by_xpath('//XCUIElementTypeButton[@name="List App"]').click()
    
    # click 'capture message' button
    btn = ios_react_native_sim_driver.find_element_by_accessibility_id("Capture Message")
    btn.click()
