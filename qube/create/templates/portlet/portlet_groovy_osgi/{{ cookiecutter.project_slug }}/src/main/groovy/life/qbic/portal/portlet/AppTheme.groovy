package life.qbic.portal.portlet

import org.osgi.service.component.annotations.Component

import com.vaadin.osgi.resources.OsgiVaadinTheme
import com.vaadin.ui.themes.ValoTheme

@Component(immediate = true, service = OsgiVaadinTheme.class)
class AppTheme extends ValoTheme implements OsgiVaadinTheme {
    @Override
    public String getName() {
        return "mytheme"
    }

}
