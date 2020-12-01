package life.qbic.portal.portlet;

import java.io.IOException;
import java.util.Properties;
import org.osgi.framework.Bundle;
import org.osgi.framework.FrameworkUtil;

/**
 * Shows the portlet information
 * <p>
 * This class can be used when the bundle description is missing
 *
 * @since: 2.6.2
 */
public class PortletInformation {

    private String portletName;
    private String portletVersion;
    private String portletRepoURL;

    public PortletInformation(){
        Bundle bundle = FrameworkUtil.getBundle({{ cookiecutter.main_class_prefix }}PortletUI.class);
        if (bundle == null) {
            tryToLoadProperties();
        } else {
            loadBundleProperties(bundle);
        }
    }

    public String getPortletName() {
        return portletName;
    }

    public String getPortletVersion() {
        return portletVersion;
    }

    public String getPortletRepoURL() {
        return portletRepoURL;
    }

    private void loadBundleProperties(Bundle bundle) {
        portletName = bundle.getHeaders().get("Bundle-Name");
        portletVersion = bundle.getVersion().toString();
        portletRepoURL =  bundle.getHeaders().get("Bundle-DocURL");
    }

    private void tryToLoadProperties() {
        try {
            loadProperties();
        } catch (IOException e){
            throw new RuntimeException(e);
        }
    }

    private void loadProperties() throws IOException {
        final Properties properties = new Properties();
        properties.load(this.getClass().getClassLoader().getResourceAsStream("app.properties"));
        portletName = properties.getProperty("name");
        portletVersion = properties.getProperty("version");
        portletRepoURL =  properties.getProperty("url");
    }
}
